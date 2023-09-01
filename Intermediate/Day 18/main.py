from turtle import *
import random
#import colorgram

screen = Screen()
screen.colormode(255)

timmy = Turtle()

timmy.shape("arrow")

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

# Random colour
def random_colour():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  random_colour = (r,g,b)
  return random_colour

# Random Walk
#directions = [0,90,180,270]

#for moves in range(200):
#  timmy.pen(pensize=7)
#  timmy.pencolor(random_colour())
#  timmy.forward(30)
#  timmy.left(directions[random.randint(0,3)])

# Spirograph with random colours
#left = 0
#while left < 360:
#  timmy.left(10)
#  timmy.pencolor(random_colour())
#  timmy.circle(100)
#  left += 10

# Hirst image
#colors = colorgram.extract('Day 18\image.jpg',30)
#rgb = []
#for color in colors:
#  r = color.rgb.r
#  g = color.rgb.g
#  b = color.rgb.b
#  new_color = (r, g, b)
#  rgb.append(new_color)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy.shapesize(.5)
timmy.penup()
timmy.setpos(-400,-300)
y = -300
while y < 300:
  timmy.setpos(-400, y)
  for x in range(15):
    timmy.fd(50)
    timmy.pendown()
    timmy.dot(20,random.choice(color_list))
    timmy.penup()
  y += 50



screen.exitonclick()
