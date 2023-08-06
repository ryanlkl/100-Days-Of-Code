from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

# Initialize objects
screen = Screen()
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# Initializing screen
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

# Creating controls
screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down,"Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collisions
    if ball.ycor() > 290 or ball.ycor() < -290:
        # Bounce
        ball.wall_bounce()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 40 and ball.xcor() > 330 or ball.distance(l_paddle) < 40 and ball.xcor() < -330:
        ball.paddle_bounce()

    # Detect goals scored
    if ball.xcor() > 390:
        ball.reset()
        r_paddle.reset((350,0))
        l_paddle.reset((-350,0))
        scoreboard.l_increment()

    if ball.xcor() < -390:
        ball.reset()
        r_paddle.reset((350,0))
        l_paddle.reset((-350,0))
        scoreboard.r_increment()

    if scoreboard.l_score == 11 or scoreboard.r_score == 11:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
