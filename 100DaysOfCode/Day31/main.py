BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random

try:
    words = pd.read_csv(".\\data\\words_to_learn.csv")
except FileNotFoundError:
    words = pd.read_csv(".\\data\\french_words.csv")
finally:
    word_dictionaries = words.to_dict(orient="records")

current_card = {}

def flip_card():
    global current_card    
    canvas.itemconfig(flash_card, image=card_back_img)
    canvas.itemconfig(card_title, cnf={"text":"English", "fill":"white" })
    canvas.itemconfig(card_word, cnf={"text":current_card["English"], "fill":"white" })
    pass

def right():
    global current_card
    word_dictionaries.remove(current_card)
    df = pd.DataFrame(word_dictionaries)
    df.to_csv(".\\data\\words_to_learn.csv", index=False)
    get_next_card()
    
def wrong():
    get_next_card()

def get_next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dictionaries)
    canvas.itemconfig(flash_card, image=card_front_img)
    canvas.itemconfig(card_title, cnf={"text":"French", "fill":"black" })
    canvas.itemconfig(card_word, cnf={"text":current_card["French"], "fill":"black" })
    flip_timer = window.after(3000, flip_card)

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file=".\\images\\card_front.png")
card_back_img = PhotoImage(file=".\\images\\card_back.png")
flash_card = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

wrong_img = PhotoImage(file=".\\images\\wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong)
wrong_button.grid(row=1, column=0)

right_img = PhotoImage(file=".\\images\\right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right)
right_button.grid(row=1, column=1)

get_next_card()
window.mainloop()