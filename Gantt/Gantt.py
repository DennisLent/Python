from datetime import datetime, timedelta

import pandas as pd

from DataClasses import Task, Phase, Deadline

import matplotlib.pyplot as plt


# datetime.fromisoformat('yyyy-mm-dd')

class GanttChart:
    """
    Generate a visualization of a Gantt Chart based on the Excel Document
    """

    @staticmethod
    def read_excel(file):
        """
        Static method to read the Excel file with phases, tasks, sub-tasks and deadlines
        :param file: Excel file in correct format
        :return: ordered_events: list of all events in order
        """
        def _date_parser(date):
            """
            Function to parse dates from the excel and convert to readable format for datetime module
            :param date: string in format DD.MM.YY
            :return: string in format YYYY-MM-DD
            """
            day, month, year = date.split(".")
            year = "20" + year
            return f"{year}-{month}-{day}"

        def _make_phase(_line):
            """
            Function to make phase object
            :param _line: col1: name | col3: start | col4: end
            :return: Phase object
            """
            name = _line["col1"].split("-")[1]
            start = datetime.fromisoformat(_date_parser(_line["col3"]))
            end = datetime.fromisoformat(_date_parser(_line["col4"])) + timedelta(hours=18)
            return Phase(name, start, end)

        def _make_deadline(_line):
            """
            Function to make deadline object
            :param _line: col1: name | col4: end
            :return: Deadline object
            """
            name = _line["col1"].split("-")[1]
            end = datetime.fromisoformat(_date_parser(_line["col4"])) + timedelta(hours=18)
            return Deadline(name, end)

        def _make_task(_line):
            """
            Function to make tasks and subtasks
            :param _line: col1: name | col2: assignee | col3: start | col4: end
            :return: Task object
            """
            if _line["col2"]:
                # has assigned people -> has time constraint
                if "s-" in _line["col1"]:
                    name = _line["col1"].split("-")[1]
                else:
                    name = _line["col1"]
                assignee = _line["col2"].split(",")
                start = datetime.fromisoformat(_date_parser(_line["col3"]))
                end = datetime.fromisoformat(_date_parser(_line["col4"])) + timedelta(hours=18)
                return Task(name, assignee, start, end)
            else:
                name = line["col1"]
                return Task(name)

        ordered_events = []
        df = pd.read_excel(file, na_filter=False)
        for num, line in df.iterrows():

            # print(line["col1"], line["col2"], line["col3"], line["col4"])

            if "p-" in line["col1"]:
                # print("phase")
                ordered_events.append(_make_phase(line))

            elif "d-" in line["col1"]:
                # print("deadline")
                ordered_events.append(_make_deadline(line))

            elif "s-" in line["col1"]:
                # print("subtask")
                subtask = _make_task(line)

                def _add_to_furthest_task(task, _subtask):
                    """
                    Function to recursively find the lowest subtask
                    :param task: current task being checked
                    :return: None
                    """
                    if task.sub is None:
                        task.sub = _subtask
                    else:
                        _add_to_furthest_task(task.sub, _subtask)

                _add_to_furthest_task(ordered_events[-1], subtask)

            else:
                # print("task")
                ordered_events.append(_make_task(line))

        for item in ordered_events:
            if type(item) == Task:
                if item.sub is not None:
                    item.update_dates()

        return ordered_events

    def __init__(self, file, name=None):
        """
        Initlializer for Gantt Chart
        :param file: Excel file in correct format
        :param name: (optinal) name of the Gantt Chart
        """

        def _find_people(events):
            """
            Function to find how many people are involved in the activites
            :param events: list of all events occuring in the Gantt Chart
            :return: people: set of all people
            """
            people = set()
            for item in events:
                if type(item) == Task:
                    if item.assignee is not None:
                        for person in item.assignee:
                            if person != "all":
                                people.add(person)
            return people

        def _assign_colors(people):
            """
            Function to create dictionary and assign each person a color
            :param people:
            :return:
            """
            color_list = ["blue", "orange", "brown", "purple", "lime", "navy", "yellow", "green", "pink", "magenta"]
            color_dict = dict(zip(people, color_list))
            return color_dict

        self.events = self.read_excel(file)

        self.people = _find_people(self.events)

        self.color_dict = _assign_colors(self.people)

        self.name = name

        self.x_ticks = []
        self.x_labels = []
        self.y_ticks = []
        self.y_labels = []

    def show(self):

        def _plot_single_task(_task, _color_dict, _height):
            """
            Function for plotting a single task (no subtasks)
            :param _task: Task
            :param _color_dict: color dictionary (object from Gantt)
            :param _height: height at which line is drawn
            :return: Pyplot object
            """
            for person in _task.assignee:
                if person != "all":
                    plt.plot([_task.start, _task.end], [_height, _height], color=_color_dict[person])
                    _height -= 1
                else:
                    for keys, vals in _color_dict.items():
                        plt.plot([_task.start, _task.end], [_height, _height], color=vals)
                        _height -= 1

            self.y_ticks.append(_height)
            self.y_labels.append(_task.name)
            self.x_ticks.append(_task.start)
            self.x_ticks.append(_task.end)

            return _height

        def _plot_multi_task(_task, _color_dict, _height):
            """
            Function for plotting a multi task (task with subtask(s))
            :param _task: Task
            :param _color_dict: color dictionary (object from Gantt)
            :param _height: height at which line is drawn
            :return: Pyplot object
            """
            if not _task.assignee:
                # task does not have assignee -> plot time overview of task
                plt.plot([_task.start, _task.end], [_height, _height], color="cyan", alpha=0.5)
                self.y_ticks.append(height)
                self.y_labels.append(_task.name)
                self.x_ticks.append(_task.start)
                self.x_ticks.append(_task.end)

                _height -= 5
            else:
                # task does have assignee
                _plot_single_task(_task, _color_dict, _height)
                _height -= 5

            if _task.sub is not None:
                # if there are more tasks recursively plot
                _height = _plot_multi_task(_task.sub, _color_dict, _height)
                return _height

            else:
                # no more tasks end
                return _height

        def _make_legend(x_max, people, color_dict):
            """
            Function to make a legend of the assigned people
            :param x_max: maximum date
            :param people: people list from Gantt Object
            :param color_dict: color_dictionary from Gantt Object
            :return: Pyplot Object
            """
            for person in people:
                plt.plot([x_max, x_max+timedelta(hours=1)], [height, height],
                         color=color_dict[person], label=f"{person}")

        # Main plotting loop
        height = 0
        for item in self.events:

            if type(item) == Phase:
                # phase is plotted first as it is the overview
                plt.plot([item.start, item.end], [height, height], color="grey", alpha=0.8)
                self.y_ticks.append(height)
                self.y_labels.append(item.name)
                self.x_ticks.append(item.start)
                self.x_ticks.append(item.end)

            if type(item) == Deadline:
                # deadline is plotted second as it sets the end
                plt.scatter(item.end, height, 15, c="red")
                self.y_ticks.append(height)
                self.y_labels.append(item.name)
                self.x_ticks.append(item.end)

            if type(item) == Task:
                # tasks are plotted last
                if item.sub is None:
                    height = _plot_single_task(item, self.color_dict, height)

                else:
                    height = _plot_multi_task(item, self.color_dict, height)

            height -= 5

        self.x_ticks = list(set(sorted(self.x_ticks)))

        plt.yticks(self.y_ticks, self.y_labels)
        plt.xticks(self.x_ticks)
        plt.xticks(rotation=90)
        plt.grid(alpha=0.4)

        left, right = sorted(self.x_ticks)[0], sorted(self.x_ticks)[-1]

        # print(f"left={left}, right={right}")

        _make_legend(right+timedelta(hours=5), self.people, self.color_dict)
        plt.xlim(left-timedelta(hours=4), right+timedelta(hours=4))
        plt.legend()

        if self.name is None:
            plt.title("My Gantt Chart")
        else:
            plt.title(self.name)

        plt.show()


if __name__ == "__main__":
    pass
