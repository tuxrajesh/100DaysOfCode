BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

words = pd.read_csv(".\\data\\french_words.csv")
word_dictionaries = words.to_dict(orient="records")
current_card = {}

def flip_card():
    global current_card    
    canvas.itemconfig(flash_card, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    pass

def get_next_word():
    global current_card 
    current_card = random.choice(word_dictionaries)
    canvas.itemconfig(flash_card, image=card_back_img)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    pass

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file=".\\images\\card_front.png")
card_back_img = PhotoImage(file=".\\images\\card_back.png")
flash_card = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file=".\\images\\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file=".\\images\\right.png")
right_button = Button(image=right_img, highlightthickness=0, command=get_next_word)
right_button.grid(row=1, column=1)

get_next_word()
window.after(3000, flip_card)
window.mainloop()