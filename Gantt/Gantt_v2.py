import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


"""MAKE A GANTT CHART: SUPPORTS UP TO 10 INDIVIDUALS"""

class Task:

    def __init__(self, Name, Start, End, Asignee=None, T1=None, T2=None):
        self.Name = Name
        self.Assignee = Asignee
        self.Start = Start
        self.End = End
        self.subtask = None
        if T1 is None and T2 is None:
            self.Start += datetime(0,0,0,9)
            self.End += datetime(0,0,0,17)
        else:
            pass

    def __str__(self):
        return f"{self.Assignee}: {self.Name}. {self.Start} --> {self.End}"

    def add_sub(self, sub):
        self.subtask = sub

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
    Phase_list = []
    Deliverable_list = []
    Task_list = []

    @staticmethod
    def read(filename):
        """0-Task, 1-Deliverable/Phase Name, 2-Assignee, 3-Start date, 4 - End date, 5-Duration (hours)"""
        df = pd.read_excel(filename, dtype=str).fillna("None")
        #print(df)
        for index, row in df.iterrows():
            print(row)

            """Phase"""
            if row[0].lower() == "phase":
                name = f"Phase {row[1]}"
                y1,m1,d1 = row[3].split(" ")[0].split("-")
                y2,m2,d2 = row[4].split(" ")[0].split("-")
                start, end = datetime(int(y1),int(m1),int(d1),9), datetime(int(y2),int(m2),int(d2),17)
                phase = Phase(name, start, end)
                Gantt.Phase_list.append(phase)

            """Deliverable"""
            if row[0].lower() == "deliverable":
                name = row[1]
                y, m, d = row[4].split(" ")[0].split("-")
                date = datetime(int(y),int(m),int(d),17)
                deliv = Deliv(name, date)
                Gantt.Deliverable_list.append(deliv)

            """Normal tasj"""
            name = row[0]
            y1, m1, d1 = row[3].split(" ")[0].split("-")
            y2, m2, d2 = row[4].split(" ")[0].split("-")
            start, end = datetime(int(y1), int(m1), int(d1)), datetime(int(y2), int(m2), int(d2))
            if df["Assignee"].all() == None:
                task = Task(name,start,end)
                print(task)







gantt = Gantt()
gantt.read("Example.xlsx")