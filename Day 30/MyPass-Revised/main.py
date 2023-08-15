from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  char_list = [choice(letters) for _ in range(randint(8,10))]

  symbols_list = [choice(symbols) for _ in range(randint(2,4))]

  char_list = [choice(numbers) for _ in range(randint(2,4))]

  password_list = char_list + symbols_list + char_list
  shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0,f"{password}")
  pyperclip.copy(f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {website: {
    "email": email,
    "password": password
  }}

  if len(website) == 0 or len(email) == 0 or len(password) == 0:
    messagebox.showinfo(title="Empty Inputs",message="Please complete all of the input fields")
  else:
      try:
        with open("Day 30\\MyPass-Revised\\data.json","r") as data_file:
          # Reading old data
          data = json.load(data_file)
      except FileNotFoundError:
         with open("Day 30\\MyPass-Revised\\data.json","w") as data_file:
            json.dump(new_data,data_file,indent=4)
      else:
        # Updating old data with new
        data.update(new_data)

        with open("Day 30\\MyPass-Revised\\data.json","w") as data_file:
          # Writing updated data to data file
          json.dump(data,data_file,indent=4)
      finally:
          website_entry.delete(0,END)
          password_entry.delete(0,END)
# --------------------------- Find Data --------------------------------#
def search():
   website = website_entry.get()

   try:
    with open("Day 30\\MyPass-Revised\\data.json","r") as data_file:
        data = json.load(data_file)
   except FileNotFoundError:
      messagebox.showinfo(title="Error", message="No Data File Found.")
   else:
      if website in data:
         email = data[website]["email"]
         password = data[website]["password"]
         messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
      else:
         messagebox.showinfo(title=website,message=f"You have nothing stored for {website}")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

img = PhotoImage(file="Day 29\\logo.png")
canvas = Canvas(width=200,height=200,highlightthickness=0)
canvas.create_image(100,100,image=img)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

# Entries
website_entry = Entry(width=31)
website_entry.grid(column=1,row=1)
website_entry.focus()
email_entry = Entry(width=48)
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0,"ryanla94@gmail.com")
password_entry = Entry(width=31)
password_entry.grid(column=1,row=3)

# Buttons
search_button = Button(text="Search",width=13,command=search)
search_button.grid(column=2,row=1,sticky="W")
password_button = Button(text="Generate",width=13,command=generate_password)
password_button.grid(column=2,row=3,sticky="W")
add_button = Button(text="Add",width=41,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()
