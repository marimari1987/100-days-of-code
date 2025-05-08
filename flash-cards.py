from tkinter import *
from tkinter import messagebox
import pandas
from random import choice
import os

BACKGROUND_COLOR = "#B1DDC6"
TIMERCOUNT = 0

# -------------- Button Functions ----------- #
try:
    data = pandas.read_csv("data/to_learn.csv")
    print(len(data))
except FileNotFoundError:
    data = pandas.read_csv("data/1000 häufigste italienische Wörter.csv")

to_learn = data.to_dict(orient="records")  # [{'Italiano': 'abbastanza', 'Deutsch': 'ganz'},
                                           # {'Italiano': 'accordo', 'Deutsch': 'Zustimmung'}
current_card = choice(to_learn)  # {'Italiano': 'parla', 'Deutsch': 'spricht'}


# vocabulary_data_frame = pandas.DataFrame(data)
# vocabulary_dict = {}  # {abbastanza: ganz, accordo: zustimmung...} war nicht so geeignet
# for (index, row) in vocabulary_data_frame.iterrows():
#     vocabulary_dict[row.Italiano] = row.Deutsch


def new_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)  # {'Italiano': 'parla', 'Deutsch': 'spricht'}
    card.itemconfig(front, image=image_front)
    card.itemconfig(word_text, text=current_card["Italiano"], fill="black")
    card.itemconfig(title_text, text="Italiano", fill="black")
    flip_timer = window.after(3000, flip_card)   # auch hier muss die id flip_timer vergeben werden


def remove_word():
    global current_card
    to_learn.remove(current_card)
    if len(to_learn) == 0:
        messagebox.showinfo(title="Herzlichen Glückwunsch", message="Du hast alle Vokabeln gelernt!")
        os.remove("data/to_learn.csv")
        window.destroy()
    else:
        new_word()


def save_files():
    if messagebox.askokcancel(title="Goodbye", message="Lernfortschritt speichern?"):
        pandas.DataFrame(to_learn).to_csv("data/to_learn.csv", index=False)
        #Dict updating is in a separate function
    window.destroy()


# ------------- flip card function ----------- #

def flip_card():
    card.itemconfig(front, image=image_back)
    card.itemconfig(word_text, text=current_card["Deutsch"], fill="white")
    card.itemconfig(title_text, text="Deutsch", fill="white")

# ---------------------- UI ------------------ #


window = Tk()
window.title("Flashcards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.protocol("WM_DELETE_WINDOW", save_files)
flip_timer = window.after(3000, flip_card, current_card)

# Canvas
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthicknes=0)
image_front = PhotoImage(file="images/card_front.png")  # darf nicht in einer Funktion kreiert werden
image_back = PhotoImage(file="images/card_back.png")
front = card.create_image(400, 264, image=image_front)
card.grid(column=0, row=0, columnspan=2)
title_text = card.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))  # das hatte ich vergessen
word_text = card.create_text(400, 264, text="Word", font=("Arial", 60, "bold"))

# Buttons
yes_image = PhotoImage(file="images/right.png")
yes_button = Button(image=yes_image, highlightthicknes=0, command=remove_word, bd=0)
yes_button.grid(column=1, row=1)
no_image = PhotoImage(file="images/wrong.png")
no_button = Button(image=no_image, highlightthicknes=0, command=new_word, bd=0)
no_button.grid(column=0, row=1)

new_word()

window.mainloop()
