import pandas as pd
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilename
import time
import itertools
import pyperclip




def run_program():
    intake = []
    mentee_responded = {}
    mentor_responded = {}
    window = Tk()
    window.title("Shepherds Form Management")
    window.geometry("850x600")

    def reset():
        window.destroy()
        run_program()

    def fill_the_list(dictionary1, dictionary2, lst_to_check):
        lst = []
        for email in lst_to_check:
            if email not in dictionary1 and email not in dictionary2:
                lst.append(email)
        return lst

    def process_intake(lst):
        interested_info = []

        for file in lst:
            with open(f"{file}", encoding='utf-8') as data:
                data = [x.split(",") for x in data.readlines() if "/" in x]
                interested_info.append(data)
        interested_in = list(itertools.chain.from_iterable(interested_info))
        intake_emails = []

        for x in interested_in:
            for y in x:
                if "@" in y:
                    intake_emails.append(y.strip())
        return intake_emails

    def process_files():
        emails = process_intake(intake)

        lst = fill_the_list(mentee_responded, mentor_responded, emails)
        if not lst:
            Label(window, text="Please select all files", foreground='blue').grid(row=5, columnspan=3, pady=10)
        for x in range(len(lst)):
            Label(window, text=f"{lst[x]}", foreground="blue").grid(row=x+7, columnspan=3, pady=10)

    def mentee_to_dict():
        global mentee_responded
        mentee_file = askopenfilename()
        mentee_feedback = pd.read_csv(mentee_file)
        mentee_file_label.config(text=f"{mentee_file}")
        mentee_names = [x.title() for x in list(mentee_feedback["Name"]) if isinstance(x, str)]
        mentee_emails = list(mentee_feedback["Email"])
        mentee_dict = {mentee_emails[x]: mentee_names[x] for x in range(len(mentee_names))}
        mentee_responded = mentee_dict

    def mentor_to_dict():
        global mentor_responded
        mentor_file = askopenfilename()
        mentor_feedback = pd.read_csv(mentor_file)
        mentor_file_label.config(text=f"{mentor_file}")
        mentor_names = [x.title() for x in list(mentor_feedback["Name"]) if isinstance(x, str)]
        mentor_emails = list(mentor_feedback["Email"])
        mentor_dict = {mentor_emails[x]: mentor_names[x] for x in range(len(mentor_names))}
        mentor_responded = mentor_dict

    def combine1():
        intake.append(askopenfilename())
        intake1_file_label.config(text=f"{intake[0]}")

    def combine2():
        intake.append(askopenfilename())
        intake2_file_label.config(text=f"{intake[1]}")

    mentor_feedback_label = Label(
        window,
        text="Upload Mentor Feedback File in csv format",
        font=("ariel", 10, "bold")
    )
    mentor_feedback_label.grid(row=0, column=0, padx=10)

    mentor_feedback_btn = Button(
        window,
        text="Choose File",
        command=lambda: mentor_to_dict()
    )
    mentor_feedback_btn.grid(row=0, column=1)

    mentor_file_label = Label(
        window,
        text=""
    )
    mentor_file_label.grid(row=0, column=2, padx=10)

    mentee_feedback_label = Label(
        window,
        text="Upload Mentee Feedback File in csv format",
        font=("ariel", 10, "bold")
    )
    mentee_feedback_label.grid(row=1, column=0, padx=10)
    mentee_feedback_btn = Button(
        window,
        text="Choose File",
        command=lambda: mentee_to_dict()
    )
    mentee_feedback_btn.grid(row=1, column=1)

    mentee_file_label = Label(
        window,
        text=""
    )
    mentee_file_label.grid(row=1, column=2, padx=10)

    intake1_label = Label(
        window,
        text="Upload First Intake File in csv format",
        font=("ariel", 10, "bold")
    )
    intake1_label.grid(row=2, column=0, padx=10)
    intake1_btn = Button(
        window,
        text="Choose File",
        command=lambda: combine1()
    )
    intake1_btn.grid(row=2, column=1)
    intake1_file_label = Label(
        window,
        text=""
    )
    intake1_file_label.grid(row=2, column=2)
    intake2_label = Label(
        window,
        text="Upload Second Intake File in csv format",
        font=("ariel", 10, "bold")
    )
    intake2_label.grid(row=3, column=0, padx=10)

    intake2_btn = Button(
        window,
        text="Choose File",
        command=lambda: combine2()
    )
    intake2_btn.grid(row=3, column=1)
    intake2_file_label = Label(
        window,
        text=""
    )
    intake2_file_label.grid(row=3, column=2)

    process_btn = Button(
        window,
        text="Process Files",
        command=process_files,
        width=100,

    )
    process_btn.grid(row=4, columnspan=3, pady=10)

    reset_button = Button(
        window,
        text="Reset",
        command=reset,
        width=50,

    )
    reset_button.grid(row=6, columnspan=3, pady=50)

    window.mainloop()


run_program()
