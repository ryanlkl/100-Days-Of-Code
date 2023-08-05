from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)

# Create snake body

starting_x = 0
segments = []

for segment in range(0,3):
    dot = Turtle(shape="square")
    dot.penup()
    dot.color("white")
    dot.goto(x=starting_x,y=0)
    segments.append(dot)
    starting_x -= 20

screen.update()

# Move snake automatically
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    for seg in segments:
        seg.forward(10)


screen.exitonclick()
