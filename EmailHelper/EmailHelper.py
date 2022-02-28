import tkinter as tk
import os
import datetime
from EmailHelperSettings import SettingWindow

def MainWindow():

    window = tk.Tk()
    window.title("Dennis' Cool Little Program")
    window.resizable(width=True, height=True)

    """Title and options"""
    label = tk.Label(text="Automated Email Helper", fg="white", bg="black", width=100, height=5)
    label.pack()

    btn_ops = tk.Button(text="OPTIONS")
    btn_ops.pack()

    """Topic of Email"""
    current_date = str(datetime.datetime.now())[0:9]
    topic_label = tk.Label(text="Topic")
    topic_entry = tk.Entry(fg="black", bg="white", width=50)
    topic_label.pack()
    topic_entry.pack()
    topic_entry.insert(0, f"Summary {current_date}")

    """Email text"""
    text_label = tk.Label(text="Enter Email Text")
    text_box = tk.Text()
    text_label.pack()
    text_box.pack()

    """send button"""
    btn_send = tk.Button(text="SEND", command=SettingWindow())
    btn_send.pack()



    window.mainloop()
