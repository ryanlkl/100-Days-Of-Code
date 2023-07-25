from turtle import *
import random

timmy = Turtle()

timmy.shape("circle")
timmy.color("blue")

# Drawing a dashed line
#for moves in range(0,50):
#    timmy.forward(3)
#    timmy.color("white")
#    timmy.forward(3)
#    timmy.color("blue")

# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon
# and decagon
# Do so by calculating inner angle and using number of sides


#outside_angle = 180 - inside_angle
#for moves in range(0,3):
#    timmy.forward(100)
#    timmy.left(120)

# Square
#for moves in range(0,4):
#  timmy.forward(100)
#  timmy.left(90)

# Pentagon
#for moves in range(0,5):
#    timmy.forward(100)
#    timmy.left(72)

# Hexagon
#for moves in range(0,6):
#    timmy.forward(100)
#    timmy.left(60)

# Heptagon
#for moves in range(0,7):#
#    timmy.forward(100)
#    timmy.left(180 - 900/7)

# Octagon
#for moves in range(0,8):
#    timmy.forward(100)
#    timmy.left(180 - 1080/8)

# Nonagon
#for moves in range(0,9):
#    timmy.fd(100)
#    timmy.left(180 - 1260/9)

# Decagon
#for moves in range(0,10):
#    timmy.fd(100)
#    timmy.left(36)

# Random Walk
screen = Screen()
screen.colormode(255)

def random_colour():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_colour = (r,g,b)
  return random_colour

directions = [0,90,180,270]

for moves in range(200):
  timmy.pen(pensize=7)
  timmy.pencolor(random_colour())
  timmy.forward(30)
  timmy.left(directions[random.randint(0,3)])


screen.exitonclick()
