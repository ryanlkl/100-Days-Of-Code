from scoreboard import Scoreboard
from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,key="Down")
screen.onkey(snake.left,key="Left")
screen.onkey(snake.right,key="Right")

# Move snake automatically
# Make segments move together by moving later segments to position of prior segment

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.04)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       scoreboard.increment()

    # Detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.xcor() <= -290 or snake.head.ycor() >= 290 or snake.head.ycor() <= -290:
        game_is_on = False
        scoreboard.game_over()

    # Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
