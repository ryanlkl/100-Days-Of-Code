from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.x_cor = 0
        self.y_cor=-270
        self.goto(self.x_cor,self.y_cor)
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=0.75,stretch_len=0.75)

    def forward(self):
        self.y_cor += 20
        self.goto(self.x_cor,self.y_cor)

    def backward(self):
        self.y_cor -= 20
        self.goto(self.x_cor,self.y_cor)

    def reset(self):
        self.x_cor = 0
        self.y_cor = -270
        self.goto(self.x_cor,self.y_cor)
