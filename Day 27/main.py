from tkinter import *

# Initialise the window
window = Tk()
window.title("Converter")
window.minsize(width=300,height=100)

def change_label_3():
    miles = float(entry.get())
    km = miles * 1.609
    label_3.config(text=f"{km}")

entry = Entry(width=20)
entry.grid(column=2,row=0)

label_1 = Label(text="miles")
label_1.grid(column=3,row=0)

label_2 = Label(text="is equal to")
label_2.grid(column=1,row=1)

label_3 = Label(text="0")
label_3.grid(column=2,row=1)

label_4 = Label(text="km")
label_4.grid(column=3,row=1)

button = Button(text="Calculate",command=change_label_3)
button.grid(column=2,row=2)

window.mainloop()
