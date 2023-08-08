from turtle import Screen
from cars import Cars
from player import Player
from scoreboard import Scoreboard
import time

# Initialising all components
screen = Screen()
cars = Cars()
player = Player()
scoreboard = Scoreboard()

#Setting up screen
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Crossing")

screen.listen()
screen.onkey(player.forward,"Up")
screen.onkey(player.backward,"Down")

# Setting up game
game_is_on = True
while game_is_on:
    cars.create_car()
    cars.move()
    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            screen.clear()
            scoreboard.lose()
    if player.y_cor > 260:
        scoreboard.increment()
        cars.reset()
        player.reset()
    screen.update()
    time.sleep(0.1)

screen.exitonclick()
