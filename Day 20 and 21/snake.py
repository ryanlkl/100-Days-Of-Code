from turtle import Turtle

START_POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        
    def create_snake(self):
        for position in START_POSITION:
            dot = Turtle(shape="square")
            dot.penup()
            dot.color("white")
            dot.goto(position)
            self.segments.append(dot)

    def move(self):
        for seg in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
          self.head.seth(UP)

    def down(self):
        if self.head.heading() != UP:
          self.head.seth(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
          self.head.seth(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
          self.head.seth(RIGHT)
