from turtle import Turtle, Screen

# Event listeners
terry = Turtle()
screen = Screen()


def move_forward():
    terry.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forward)

screen.exitonclick()
