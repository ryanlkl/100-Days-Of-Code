BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas
import random

# Read from vocab list
try:
    data_file = pandas.read_csv("Day 31\\data\\words_to_learn.csv")
except FileNotFoundError:
    data_file = pandas.read_csv("Day 31\\data\\french_words.csv")
    lang_dict = data_file.to_dict(orient="records")
else:
    lang_dict = data_file.to_dict(orient="records")
current_card = {}
# --------------------------- Words to Learn ------------------------- #

def is_known():
    # Get the word that was previously on
    # Remove from old list
    # Update new list to words_to_learn.csv
    lang_dict.remove(current_card)
    data = pandas.DataFrame(lang_dict)
    data.to_csv("Day 31\\data\\words_to_learn.csv",index=False)
    change_word()

# ----------------------- Create New Flash Cards ---------------------- #

def change_word():
    # Insert variables as global variables
    global current_card
    global flip_timer
    window.after_cancel(flip_timer) # Cancel the previous timer
    current_card = random.choice(lang_dict) # Choose new random word from data
    card.itemconfig(card_word, text=current_card["French"], fill="black") # Change card to new french word
    card.itemconfig(card_language, text="French", fill="black") # Change language title back to French
    card.itemconfig(card_background, image=card_img) # Change canvas bg to the front of the card
    flip_timer = window.after(3000,func=flip_card) # Set a timer to flip the card after 3 seconds

# ------------------------- Flipping Flashcard ------------------------ #
def flip_card():
    card.itemconfig(card_language, text="English",fill="white") # Change language title to "English"
    card.itemconfig(card_word,text=current_card["English"],fill="white") # Change French word to its translation
    card.itemconfig(card_background,image=card_back_img)

# --------------------------- User Interface -------------------------- #

window = Tk() # Initialise the window
window.title("Flashcards") # Add title to the window
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50) # Configure bg color and padding

flip_timer = window.after(3000,func=flip_card)

# Card
# Upload card background images and save to variables
card_img = PhotoImage(file="Day 31\\images\\card_front.png")
card_back_img = PhotoImage(file="Day 31\\images\\card_back.png")
# Initialise canvas
card = Canvas(bg=BACKGROUND_COLOR,width=800,height=526,highlightthickness=0)
card_background = card.create_image(400,263,image=card_img,tags="front")
card_language = card.create_text(400,150,text="French",font=("Arial",30,"italic"),tags="language")
card_word = card.create_text(400,263,text=f"Word",font=("Ariel",50,"bold"),tags="word")
card.grid(column=0,row=0,columnspan=2)

# Buttons
wrong_img = PhotoImage(file="Day 31\\images\\wrong.png")
wrong_button = Button(image=wrong_img,highlightthickness=0,command=change_word)
wrong_button.grid(column=0,row=1)
right_img = PhotoImage(file="Day 31\\images\\right.png")
right_button = Button(image=right_img,highlightthickness=0,command=is_known)
right_button.grid(column=1,row=1)

change_word()








window.mainloop()
