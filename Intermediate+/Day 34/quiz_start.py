from tkinter import ttk
from tkinter import *
from ui import QuizInterface

THEME_COLOR = "#375362"

class QuizStart:

    def __init__(self,root: Tk):
        self.window = root
        self.window.title("Quizzler")
        self.window.minsize(200,200)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.category_label = Label(
            root,
            fg="white",
            bg=THEME_COLOR,
            text="Categories"
        )
        self.category_label.grid(row=1,column=0,pady=10,padx=5)

        self.category_select = ttk.Combobox(
            root,
            state="readonly",
            values=["General Knowledge","Entertainment: Books","Entertainment: Film","Entertainment: Music","Entertainment: Musicals & Theatres","Entertainment: TV","Entertainment: Video Games","Entertainment: Board Games","Science & Nature","Science: Computers","Science: Mathematics","Mythology","Sports","Geography","History","Politics","Art","Celebrities","Animals","Vehicles","Entertainment: Comics","Science: Gadgets","Entertainment: Japanese Anime & Manga","Entertainment: Cartoon & Animations"]
        )
        self.category_select.grid(row=1,column=1,pady=10,padx=5)

        self.difficulty_label = Label(
            root,
            fg="white",
            bg=THEME_COLOR,
            text="Difficulty"
        )
        self.difficulty_label.grid(row=2,column=0,pady=10,padx=5)

        self.difficulty_select = ttk.Combobox(
            root,
            state="readonly",
            values=["Easy","Medium","Hard"]
        )
        self.difficulty_select.grid(row=2,column=1,pady=10,padx=5)

        self.no_question_label = Label(
            root,
            fg="white",
            bg=THEME_COLOR,
            text="Number of Questions"
        )
        self.no_question_label.grid(row=3,column=0,pady=10,padx=5)

        self.no_questions_select = Spinbox(
           root,
           from_=1,
           to_=100
        )
        self.no_questions_select.grid(row=3,column=1,pady=10,padx=5)

        self.continue_button = Button(
            width=20,
            text="Play",
            command=self.start_quiz,
            highlightthickness = 0
        )
        self.continue_button.grid(row=4,column=0,columnspan=2,pady=10,padx=5)


    def start_quiz(self):
        no_questions = int(self.no_questions_select.get())
        category = self.category_select.get()
        difficulty = self.difficulty_select.get()

        quiz_window = QuizInterface(root=self.window,category=category,difficulty=difficulty,no_questions=no_questions)
        print("Opened quiz_window")
        for widget in self.window.winfo_children():
            widget.destroy()
        quiz_window.show()
