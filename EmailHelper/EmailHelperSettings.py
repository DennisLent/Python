import tkinter as tk

def SettingWindow():
    window1 = tk.Tk()
    window1.title("Settings for Dennis' Cool Little Program")
    window1.resizable(width=True, height=True)

    topic_label = tk.Label(text="Your Email")
    topic_entry = tk.Entry(fg="black", bg="white", width=50)
    topic_label.pack()
    topic_entry.pack()

    topic_label = tk.Label(text="Your Password")
    topic_entry = tk.Entry(fg="black", bg="white", width=50)
    topic_label.pack()
    topic_entry.pack()
