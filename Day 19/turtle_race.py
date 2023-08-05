from turtle import Turtle, Screen
import random

# import the screen

screen = Screen()

# Change colors of the turtles

color = ["Blue","Orange","Purple","Red"]

# create turtles
y_position = [45, 15, -15, -45]
all_turtles = []

for turtle_index in range(0,4):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-365,y=y_position[turtle_index])
    all_turtles.append(new_turtle)


# Dimensions of the screen

screen.setup(width=750,height=400)

# Betting

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: (blue/orange/purple/red) ")

# Race start

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
            is_race_on = False



screen.exitonclick()
