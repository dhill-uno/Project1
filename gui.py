import csv
from tkinter import *
from tkinter import messagebox
import pandas as pd


class GUI:
    def __init__(self, window):
        """
        - The code provided is meant to guide you on the dimensions used and variable names standards.
        - Add the widgets responsible for the name, status, and save button.
        """
        self.window = window

        self.frame_name = Frame(self.window)
        self.label_name = Label(self.frame_name, text='Name')
        self.entry_name = Entry(self.frame_name)
        self.label_name.pack(padx=5, side='left')
        self.entry_name.pack(padx=5, side='left')
        self.frame_name.pack(anchor='w', pady=10)

        self.frame_score = Frame(self.window)
        self.label_score = Label(self.frame_score, text="Score")
        self.entry_score = Entry(self.frame_score)
        self.label_score.pack(padx=5, side='left')
        self.entry_score.pack(padx=8, side='left')
        self.frame_score.pack(anchor='w', pady=10)

        self.frame_button = Frame(self.window)
        self.button_save = Button(self.frame_button, text="SAVE", command=self.clicked_save)
        self.button_avg = Button(self.frame_button, text="AVERAGE", command=self.clicked_avg)
        self.button_save.pack()
        self.button_avg.pack()
        self.frame_button.pack()

        self.frame_text = Frame(self.window)
        self.text = Text(self.frame_text)
        self.text.pack()

    def clicked_save(self):
        """
        Retrieve the name and score values.
        Gives a grade based on the score values
        Open the scores.csv file and append the new name, score and grade
        Clears the name and score values that were entered
        Shows the average of all scores when average button clicked
        """
        score = int(self.entry_score.get())
        try:
            assert 0 <= score <= 100
        except AssertionError:
            messagebox.showerror('Error', 'Please enter an integer from 0-100')
            quit()

        if 90 <= score <= 100:
            grade = "A"
        elif 80 <= score < 90:
            grade = "B"
        elif 70 <= score < 80:
            grade = "C"
        elif 60 <= score < 70:
            grade = "D"
        elif 0 <= score < 60:
            grade = "F"

        student_info = ['Student', 'Score', 'Grade']
        scores = [{'Student': self.entry_name.get(), 'Score': (int(self.entry_score.get())), 'Grade': grade}]

        with open("Scores.csv", "a+", newline="") as file:
            w = csv.DictWriter(file, fieldnames=student_info)
            w.writerows(scores)

        self.entry_name.delete(0, END)
        self.entry_score.delete(0, END)

    def clicked_avg(self):
        file = pd.read_csv("Scores.csv", header=0)
        mean = round(file['Score'].mean(), 2)
        messagebox.showinfo('Average Scores', f"The averages scores is {mean}")
