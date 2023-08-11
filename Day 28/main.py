from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
   window.after_cancel(timer)
   timer_title.config(text="Timer",fg=GREEN)
   canvas.itemconfig(timer_text,text="00:00")
   check_marks.config(text="")
   global reps
   reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
   global reps
   reps += 1

   work_sec = WORK_MIN * 60
   short_break_sec = SHORT_BREAK_MIN * 60
   long_break_sec = LONG_BREAK_MIN * 60

   if reps % 8 == 0:
      timer_title.config(text="Long Break",fg=RED)
      countdown(long_break_sec)
   elif reps % 2 == 0:
      timer_title.config(text="Short Break",fg=PINK)
      countdown(short_break_sec)
   else:
      timer_title.config(text="Work",fg=GREEN)
      countdown(work_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    min = int(count/60)
    seconds = count % 60
    if seconds < 10:
       seconds = f"0{seconds}"

    canvas.itemconfig(timer_text,text=f"{min}:{seconds}")
    if count > 0:
      global timer
      timer = window.after(1000,countdown, count - 1)
    else:
       start_timer()
       marks = ""
       work_sessions = int(reps/2)
       for _ in range(work_sessions):
          marks += "✔"
       check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
# Initialise window
window = Tk()
window.title("Pomodoro Study Technique")
window.config(padx=100,pady=75,bg=YELLOW)

# Import image using canvas
canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="Day 28\\tomato.png")
canvas.create_image(100,112,image=tomato)


# Display text
timer_text = canvas.create_text(100,130,text="00:00",font=(FONT_NAME,30,"bold"),fill="white")
canvas.grid(column=1,row=1)


# Create labels
timer_title = Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,35,"bold"))
timer_title.grid(column=1,row=0)
check_marks = Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,17,"normal"))
check_marks.grid(column=1,row=3)


# Create buttons
start = Button(text="Start",highlightthickness=0,command=start_timer)
reset = Button(text="Reset",highlightthickness=0,command=reset_timer)
start.grid(column=0,row=2)
reset.grid(column=2,row=2)





window.mainloop()
