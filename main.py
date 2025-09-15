from tkinter import *
import pandas 
import random
import os

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

try:
    data = pandas.read_csv("./data/french_words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")
words_to_learn = data.to_dict(orient="records")
current_card = {}

def is_known():
    words_to_learn.remove(current_card)
    to_learn_data = pandas.DataFrame(words_to_learn)
    to_learn_data.to_csv("./data/french_words_to_learn.csv", index=False)


def flip_card(event):
    global pass_img, current_card
    if len(words_to_learn) == 0:
        canvas.itemconfig(card_vocab, fill="white")
    else:
        canvas.itemconfig(card_vocab, text=current_card["English"], fill="white")
        correct_button.config(state=NORMAL)
        wrong_button.config(state=NORMAL)
    pass_img = PhotoImage(file="images/card_back.png")
    canvas.itemconfig(card_image, image=pass_img)
    canvas.itemconfig(card_title, text="English", fill="white")

def next_card(is_correct):
    global pass_img, current_card
    # add the new row to a file
    if is_correct:
        is_known()
    
    if len(words_to_learn) == 0:
        canvas.itemconfig(card_vocab, text="Congratulations! 🥳\nThere are no more\n   words to study.", fill="black", font=(FONT_NAME, 40, "italic"))
        os.remove("./data/french_words_to_learn.csv")
    else:
        current_card = random.choice(words_to_learn)
        canvas.itemconfig(card_vocab, text=current_card["French"], fill="black")
    pass_img = PhotoImage(file="images/card_front.png")
    canvas.itemconfig(card_image, image=pass_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    correct_button.config(state=DISABLED)
    wrong_button.config(state=DISABLED)

# ---------------------------- UI ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
pass_img = PhotoImage(file="images/card_front.png")
card_image = canvas.create_image(400, 263, image=pass_img)
canvas.grid(column=0, row=0, columnspan=2)

# Word
card_title = canvas.create_text(400, 150, font=(FONT_NAME, 35, "italic"))
card_vocab = canvas.create_text(400, 260, font=(FONT_NAME, 50, "bold"))
canvas.bind("<Button-1>", flip_card)

# Correct Button
correct_image = PhotoImage(file="images/right.png")
correct_button = Button(image=correct_image, highlightthickness=0, command=lambda: next_card(True), bg=BACKGROUND_COLOR)
correct_button.grid(column=0, row=1)


# Wrong Button
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=lambda: next_card(False), bg=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)

next_card(False)

window.mainloop()