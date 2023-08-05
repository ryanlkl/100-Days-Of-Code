from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

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
    time.sleep(0.05)

    snake.move()


screen.exitonclick()
