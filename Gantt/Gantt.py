import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates
from datetime import date
import datetime

"""MAKE A GANTT CHART: SUPPORTS UP TO 10 INDIVIDUALS"""

class Task:
    def __init__(self, Name, Asignee, Start, End):
        self.Name = Name
        self.Assignee = Asignee
        self.Start = Start
        self.End = End

    def __str__(self):
        return f"{self.Assignee}: {self.Name}. {self.Start} --> {self.End}"

class Phase:
    def __init__(self, Name, Start, End):
        self.Name = Name
        self.Start = Start
        self.End = End

    def __str__(self):
        return f"{self.Name}: {self.Start} --> {self.End}"

class Deliv:
    def __init__(self, Name, Date):
        self.Name = Name
        self.Date = Date

    def __str__(self):
        return f"{self.Name} | {self.Date}"


class Gantt:
    Tasks = []
    Individuals = set()
    Color_person = []
    num_tasks = None
    All_days = set()
    Phases = []
    Delivs = []


    @staticmethod
    def read(filename):
        df = pd.read_excel(filename)
        #print(df)

        """Get phases and add to internal list"""
        Phases = df.loc[df["Task Name"] == "Phase"]
        i = 1
        ind_phases = []
        for index, row in Phases.iterrows():
            p = Phase(f"{row[0]} {i}", date.fromisoformat(str(row[2]).split(" ")[0]), date.fromisoformat(str(row[3]).split(" ")[0]))
            ind_phases.append(index)
            Gantt.Phases.append(p)
            i += 1

        df = df.drop(ind_phases)

        """Get Deliverables and add to internal list"""
        Delivs = df.loc[df["Task Name"] == "Deliverable"]
        ind_delivs = []
        for index, row in Delivs.iterrows():
            d = Deliv(row[1], date.fromisoformat(str(row[3]).split(" ")[0]))
            Gantt.Delivs.append(d)
            ind_delivs.append(index)

        df = df.drop(ind_delivs)

        #print(df)

        """Get tasks and add to internal list"""
        Names = [x for x in df["Task Name"]]
        Assignees = [list(x.split(",")) for x in df["Assignee"]]
        for lst in Assignees:
            for x in lst:
                Gantt.Individuals.add(x.strip())
        Start = [date.fromisoformat(str(x).split(" ")[0]) for x in df["Start date"]]
        Gantt.All_days.update(Start)
        End = [date.fromisoformat(str(x).split(" ")[0]) for x in df["End date"]]
        Gantt.All_days.update(End)
        Gantt.All_days = sorted(Gantt.All_days)

        """Check if a task is a single day"""
        for i in range(len(Names)):
            if Start[i] == End[i]:
                End[i] += datetime.timedelta(days = 1)

            """Add tasks to the internal list"""
            task = Task(Names[i], Assignees[i], Start[i], End[i])
            Gantt.Tasks.append(task)

    """Give each person a color"""
    def assign_colors(self):
        if len(Gantt.Individuals) > 10:
            raise ValueError("Too many people in the document: only up to 10 people supported")
        cols = ["red", "blue", "green", "purple", "yellow", "cyan", "orange", "navy", "lime", "magenta"]
        people_numbers = enumerate(Gantt.Individuals)
        for person in people_numbers:
            Gantt.Color_person.append((person[1], cols[person[0]]))

    """Graph the phases with task and deliverables in between"""
    def graph(self):
        i = 1000
        y_axis = [] #i values (heights)
        y_values = [] #name of the tasks

        phase_to_remove = []
        for phase in Gantt.Phases:
            plt.plot([phase.Start, phase.End], [i,i], lw=2, color="grey")
            y_axis.append(i)
            y_values.append(phase.Name)
            i -= 10
            phase_to_remove.append(phase)

            task_to_remove = []
            for task in Gantt.Tasks:

                if task.End <= phase.End:

                    if len(task.Assignee) > 1:
                        i_init = i
                        for person in task.Assignee:
                            index = list(Gantt.Individuals).index(person.strip())
                            cp = Gantt.Color_person[index][1]
                            plt.plot([task.Start, task.End], [i, i], lw=3, color=cp, label=person.strip())
                            i -= 1
                        mid = (i_init + i) / 2
                        y_axis.append(mid)
                        y_values.append(task.Name)
                        task_to_remove.append(task)

                    else:
                        person = task.Assignee[0]
                        index = list(Gantt.Individuals).index(person.strip())
                        cp = Gantt.Color_person[index][1]
                        plt.plot([task.Start, task.End], [i, i], lw=3, color=cp, label=person.strip())
                        y_axis.append(i)
                        y_values.append(task.Name)
                        task_to_remove.append(task)
                    i -= 5
            for t in task_to_remove:
                Gantt.Tasks.remove(t)


            for deliv in Gantt.Delivs:
                deliv_to_remove = []
                if deliv.Date <= phase.End:
                    plt.scatter(deliv.Date, i, marker="o", color="deeppink", s=20)
                    y_axis.append(i)
                    y_values.append(deliv.Name)
                    deliv_to_remove.append(deliv)
                    i -= 5
                for deliv in deliv_to_remove:
                    Gantt.Delivs.remove(deliv)


        plt.yticks(y_axis, y_values)
        plt.xticks(Gantt.All_days, rotation=90)
        plt.grid(color="grey", linestyle="--", alpha=0.3)
        plt.show()


""" 
        y_axis = []
        for phase in Gantt.Phases:
            plt.plot([phase.Start, phase.End], [i, i], lw=2, color="grey")
        for task in Gantt.Tasks:
            if len(task.Assignee) > 1:
                i_init = i
                for person in task.Assignee:
                    index = list(Gantt.Individuals).index(person.strip())
                    cp = Gantt.Color_person[index][1]
                    plt.plot([task.Start, task.End], [i, i], lw=3, color=cp, label=person.strip())
                    i -= 1
                mid = (i_init + i)//2
                y_axis.append(mid)
            else:
                person = task.Assignee[0]
                index = list(Gantt.Individuals).index(person.strip())
                cp = Gantt.Color_person[index][1]
                plt.plot([task.Start, task.End], [i,i], lw=3, color=cp, label=person.strip())
                y_axis.append(i)
            i -= 5
        y_values = [task.Name for task in Gantt.Tasks]
        #print(f"y_axis: {y_axis}, y_values: {y_values}")
        plt.yticks(y_axis, y_values)
        plt.grid(axis="x", color="grey", linestyle="--")
        #plt.legend()
        plt.show()
"""


"""TEST"""

gantt = Gantt()
gantt.read("Example.xlsx")
print(gantt.Tasks)
gantt.assign_colors()
print(gantt.Color_person)
print(Gantt.All_days)
gantt.graph()

