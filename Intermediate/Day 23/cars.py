from turtle import Turtle
import random

COLOURS = ["blue","green","red","orange"]

class Cars(Turtle):

    def __init__(self):
      super().__init__()
      self.all_cars = []
      self.speed = 5
      self.penup()
      self.hideturtle()

    def create_car(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.x_pos = 300
        new_car.y_pos = random.randrange(-250,260,40)
        new_car.goto(new_car.x_pos,new_car.y_pos)
        new_car.color(random.choice(COLOURS))
        new_car.shape("square")
        new_car.shapesize(stretch_len=2)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
          car.backward(self.speed)

    def reset(self):
       self.clear()
       self.x_pos = 290
       self.speed += 0.2
