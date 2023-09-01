def add(*args):
  sum = 0
  for num in args:
    sum += num
  return sum

print(add(3,4,5,6,7,8,9,))

def calculate(num,**kwargs):
  num += kwargs["add"]
  num *= kwargs["multiply"]
  return num

print(calculate(2,add=3,multiply=5))

class Car:

  def __init__(self,**kw):
    self.make = kw["make"]
    self.model = kw.get("model")

my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)
