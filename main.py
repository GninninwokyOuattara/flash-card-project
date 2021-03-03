BACKGROUND_COLOR = "#B1DDC6"

from card import Card
from buttons import BtnRight, BtnWrong
from words import Words
from tkinter import Tk, Canvas, PhotoImage, Button, Label
import pandas
from time import sleep

timer = None


def runner():
    global timer
    word_data.random_index()
    en = word_data.df["English"][word_data.index]
    fr = word_data.df["French"][word_data.index]

    card.show_front(en)
    timer = window.after(3000, reveal, fr)

def reveal(word):
    global timer

    card.show_back(word)
    timer = window.after(3000, runner)

def confirm(e):
    if word_data.index not in word_data.knowed_index:
        word_data.knowed_index.append(word_data.index)
    print(word_data.knowed_index)
    window.after_cancel(timer)
    runner()

def unknown(e):
    global timer
    window.after_cancel(timer)
    runner()


word_data = Words()

window  = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)
window.grid_columnconfigure(0, weight = 0,minsize=100)
window.grid_columnconfigure(1, weight = 0, minsize = 500)
window.grid_columnconfigure(2, weight = 0,minsize=100)
card = Card()


btnRight = BtnRight(confirm)
btnWrong = BtnWrong(unknown)





runner()
window.mainloop()