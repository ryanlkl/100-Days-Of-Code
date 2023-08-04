from turtle import Turtle, Screen

terry = Turtle()
screen = Screen()

def forward():
    terry.forward(10)

def backward():
    terry.backward(10)

def counterclockwise():
    terry.left(11.25)

def clockwise():
    terry.right(11.25)

def clear():
    terry.clear()
    terry.penup()
    terry.home()
    terry.pendown()


screen.listen()
screen.onkey(fun=forward,key="w")
screen.onkey(fun=backward,key="s")
screen.onkey(fun=counterclockwise,key="a")
screen.onkey(fun=clockwise,key="d")
screen.onkey(fun=clear,key="c")

screen.exitonclick()
