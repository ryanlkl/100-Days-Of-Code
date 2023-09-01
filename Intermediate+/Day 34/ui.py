from tkinter import ttk
from tkinter import *
from quiz_brain import QuizBrain
from data import Data

THEME_COLOR = "#375362"

class QuizInterface():

    def __init__(self,category,difficulty,no_questions,root: Tk):
        self.window = root
        self.window.title("Quizzler")
        self.window.minsize(200,200)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.no_questions = int(no_questions)
        self.category = category
        self.difficulty = difficulty

        self.quiz = None
        self.score_label = None
        self.canvas = None
        self.true_image = None
        self.false_image = None
        self.true_button = None
        self.false_button = None

    def show(self):
        questions = Data(self.category,self.no_questions,self.difficulty)
        question_bank = questions.send_request()
        self.quiz = QuizBrain(question_bank)
        self.create_ui()

    def create_ui(self):
        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR,
            font=("Arial",13,"bold"))
        self.score_label.grid(row=0,column=1)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"Question",
            fill=THEME_COLOR,
            font=("Arial",17,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.true_image = PhotoImage(file="Day 34\\images\\true.png")
        self.false_image = PhotoImage(file="Day 34\\images\\false.png")
        self.true_button = Button(image=self.true_image,highlightthickness=0,command=self.true_pressed)
        self.false_button = Button(image=self.false_image,highlightthickness=0,command=self.false_pressed)
        self.true_button.grid(row=2,column=0)
        self.false_button.grid(row=2,column=1)

        self.get_next_question()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
          self.score_label.config(text=f"Score: {self.quiz.score}")
          q_text = self.quiz.next_question()
          self.canvas.itemconfig(self.question_text,text=q_text)
        else:
          self.canvas.itemconfig(self.question_text,text=f"Quiz Over!\nYour score is {self.quiz.score}/{self.no_questions}")
          self.true_button.config(state="disabled")
          self.false_button.config(state="disabled")


    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
