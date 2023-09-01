from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.move_speed = 0.008
        self.x_move = 1
        self.y_move = 1

    def create_ball(self):
        self.shape("square")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def wall_bounce(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def paddle_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.paddle_bounce()
        self.move_speed = 0.1
