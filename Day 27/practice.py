# Use  to create a Graphical User Interface
from tkinter import *

window = Tk()

# Initiate window
window.title("Converter GUI")
window.minsize(width=600,height=600)

# Initiate components
my_label = Label(text="Label",font=("courier",24,"bold"))
my_label.pack() # Places and automatically centres component (Have to use this to show component)

# Button
def clicked():
    text = input.get()
    my_label.config(text=f"{text}")


button = Button(text="Click me!",command=clicked)
button.place(x=200,y=400)

# Input
input = Entry(width=10)
input.place(x=400,y=200)

# grid
# Can divide screen into rows and columns
# element.grid(column=x,row=y)



# This line always has to be placed at the end of the code
window.mainloop()
