# import class from module
from turtle import Turtle, Screen
#Create a new class
lord_voldetort = Turtle()

print(lord_voldetort) # <turtle.Turtle object at 0x0000021099357ED0>
lord_voldetort.shape("turtle")
lord_voldetort.color("blue")
lord_voldetort.forward(100)

#format of attribute from object is: "object.attribute"

# Create screen
my_screen = Screen()
# Example of object.attribute
print(my_screen.canvheight)

# Object also has functions (known as methods)
# "object.method()"
my_screen.exitonclick()

#This creates a table
print("| Pokemon Name | Type |")
print("------------------------")

#can use pypi to find packages that can do this for you
# pypi is open source
# first installl into python
# to do this:
 # 1. Locate Python path
 # 2. Copy Path before Python
 # 3. Open terminal
 # 4. cd to file location
# 5. Update pip and install packages (python -m pip install --upgrade pip)
# 6. Wait for pip to upgrade
# cd Scripts
# pip install "package name"
# Open VS Code and press "shift+ctrl+p": "Python: Select Interpreter"
