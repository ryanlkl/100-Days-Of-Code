from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

  def __init__(self,):
    super().__init__()
    self.hideturtle()
    self.penup()
    self.goto(-240,260)
    self.score = 0
    self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

  def increment(self):
    self.score += 1
    self.clear()
    self.write(f"Score: {self.score}", font=FONT, align=ALIGN)

  def lose(self):
    self.goto(0,0)
    self.write(f"You Lose!\nScore: {self.score}", align=ALIGN, font=FONT)
