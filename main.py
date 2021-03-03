BACKGROUND_COLOR = "#B1DDC6"

from card import Card
from buttons import BtnRight, BtnWrong
from words import Words
from tkinter import Tk, Canvas, PhotoImage, Button, Label
import pandas
from time import sleep


def runner():
    word_data.random_index()
    en = word_data.df["English"][word_data.index]
    fr = word_data.df["French"][word_data.index]

    card.show_front(en)
    window.after(3000, reveal, fr)

def reveal(word):
    card.show_back(word)
    window.after(3000, runner)



word_data = Words()

window  = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)
window.grid_columnconfigure(0, weight = 0,minsize=100)
window.grid_columnconfigure(1, weight = 0, minsize = 500)
window.grid_columnconfigure(2, weight = 0,minsize=100)
card = Card()
# card.set_word(word_data["French"][word_data.index])
# sleep(3)
# card.set_word(word_data.french_word)
# card.toogle_card()

btnRight = BtnRight()
btnWrong = BtnWrong()



# def printH(e):
#     print("Hello World")
#     print(e)
# btnTest = Label(text = "Hello",image = image,bg=BACKGROUND_COLOR)
# btnTest.bind("<Button-1>", printH)
# btnTest.grid(column=1, row=2)



runner()
window.mainloop()