from datetime import datetime, date, timedelta

class Task:

    def __init__(self, name, assignee=None, start=None, end=None, sub=None):
        self.name = name
        self.assignee = assignee
        self.start = start
        self.end = end
        self.sub = sub

        if self.start is not None and self.end is not None and self.start == self.end:
            self.end = self.start + timedelta(hours=18)

    def __str__(self):
        if self.sub is None:
            return f"TASK: {self.name} with {self.assignee} from {self.start} to {self.end}"
        else:
            return f"TASK: {self.name} with {self.assignee} from {self.start} to {self.end}| " + str(self.sub)

    def update_dates(self):
        """
        Function to update start & end date for tasks with sub-tasks
        :return: None
        """
        if self.sub is None:
            pass
        else:

            self.start = self.sub.start

            def _furthest_task(task):
                """
                Function to recursively find the lowest subtask
                :param task: current task being checked
                :return: sub-task if available
                """
                if task.sub is None:
                    return task
                else:
                    return _furthest_task(task.sub)

            end_task = _furthest_task(self)
            self.end = end_task.end

class Phase:

    def __init__(self, name, start=None, end=None):
        self.name = name
        self.start = start
        self.end = end

    def __str__(self):
        return f"PHASE: {self.name} from {self.start} to {self.end}"


class Deadline:

    def __init__(self, name, end=None):
        self.name = name
        self.end = end

    def __str__(self):
        return f"DEADLINE: {self.name} at {self.end}"

if __name__ == "__main__":
    print("-------TEST FOR TASK--------------")
    t1 = Task("t1")
    t1_sub1 = Task("t1_sub1", None, datetime.fromisoformat("2022-02-18"), datetime.fromisoformat("2022-02-19"))
    t1_sub2 = Task("t1_sub2", None, datetime.fromisoformat("2022-02-18"), datetime.fromisoformat("2022-02-20"))
    t1_sub3 = Task("t1_sub3", None, datetime.fromisoformat("2022-02-19"), datetime.fromisoformat("2022-02-22"))
    t1.sub = t1_sub1
    t1_sub1.sub = t1_sub2
    t1_sub2.sub = t1_sub3

    print(t1)
    t1.update_dates()
    print(t1)

    print(type(t1) == Task)