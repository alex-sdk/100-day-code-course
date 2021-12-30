from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
word = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/french_words.csv')
    data_list_dict = original_data.to_dict(orient='records')
else:
    data_list_dict = data.to_dict(orient='records')

def next_card():
    global word, flip_timer
    window.after_cancel(flip_timer)
    word = random.choice(data_list_dict)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=word['French'], fill='black')
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=change_card)

def change_card():
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=word['English'], fill='white')
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    data_list_dict.remove(word)
    data = pandas.DataFrame(data_list_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title('Flashcard')
window.config(padx=50, pady=50, bg=(BACKGROUND_COLOR))
flip_timer = window.after(3000, func=change_card)

card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')
wrong_img = PhotoImage(file='images/wrong.png')
checkmark_img = PhotoImage(file='images/right.png')

canvas = Canvas(width=800, height=525, bg=(BACKGROUND_COLOR), highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)
card_background = canvas.create_image(400, 265, image=card_front_img)
card_title = canvas.create_text(400, 150, text='French', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(400, 263, text='word', font=('Arial,', 60, 'bold'))

correct_button = Button(image=checkmark_img, highlightthickness=0, command=is_known)
correct_button.grid(row=1,column=1)
wrong_button = Button(image=wrong_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()