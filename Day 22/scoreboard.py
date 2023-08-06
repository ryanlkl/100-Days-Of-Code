from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Left Score: {self.l_score} | Right Score: {self.r_score}", align=ALIGN, font=FONT)


    def r_increment(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def l_increment(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over!\nLeft: {self.l_score}/nRight:{self.r_score}", align=ALIGN, font=FONT)
        if self.l_score > self.r_score:
            self.write(f"Game Over!\nLeft: {self.l_score}/nRight:{self.r_score}\nLeft wins!", align=ALIGN, font=FONT)
        elif self.l_score < self.r_score:
            self.write(f"Game Over!\nLeft: {self.l_score}/nRight:{self.r_score}\nRight wins!", align=ALIGN, font=FONT)
        else:
            self.write(f"Game Over!\nLeft: {self.l_score}/nRight:{self.r_score}\nDraw!", align=ALIGN, font=FONT)
