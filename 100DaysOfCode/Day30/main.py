from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

FILENAME = "entries.json"

# --- GENERATE A RANDOM PASSWORD --#
def generate_password():    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    characters = []
    characters.extend(choice(letters) for _ in range(randint(8, 10)))
    characters.extend(choice(symbols) for _ in range(randint(2, 4)))
    characters.extend(choice(numbers) for _ in range(randint(2, 4)))
    shuffle(characters)

    password = "".join(characters)
    password_entry.insert(0, password)
    return 

# --- SAVE ENTRIES TO A FILE --#
def save_to_file():
    website = website_entry.get()
    email = email_name_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Error", message="Please ensure all entries are added")
    else:
        new_data = {
            website: {
                "email": email,
                "password":password
            }
        }        
        with open(file=FILENAME, mode="w") as json_file:
            try:
                file_content = json.load(json_file)                
            except:
                json.dump(new_data, json_file, indent=4)
            else:
                file_content.update(new_data)                
                json.dump(file_content, json_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# --- UI SETTINGS --#
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website :", justify='right')
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()

search_button = Button(text="Search", width=21)
search_button.grid(column=2, row=1)

email_name_label = Label(text="Email/Username :", justify='right')
email_name_label.grid(column=0, row=2)
email_name_entry = Entry(width=35)
email_name_entry.grid(column=1, row=2, columnspan=2)
email_name_entry.insert(0, "tuxrajesh@gmail.com")

password_label = Label(text="Password :", justify='right')
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save_to_file)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()