BACKGROUND_COLOR = "#B1DDC6"

from card import Card
from buttons import BtnRight, BtnWrong
from tkinter import Tk, Canvas, PhotoImage, Button, Label

window  = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)
window.configure(bg=BACKGROUND_COLOR)
window.grid_columnconfigure(0, weight = 0,minsize=100)
window.grid_columnconfigure(1, weight = 0, minsize = 500)
window.grid_columnconfigure(2, weight = 0,minsize=100)
card = Card()
# card.grid(column=1, row=0)

image = PhotoImage(file="./images/right.gif")
btnRight = BtnRight()
btnWrong = BtnWrong()



# def printH(e):
#     print("Hello World")
#     print(e)
# btnTest = Label(text = "Hello",image = image,bg=BACKGROUND_COLOR)
# btnTest.bind("<Button-1>", printH)
# btnTest.grid(column=1, row=2)

# btnRight.grid(column=1, row=1, sticky="W")
# canvas = Canvas(width=810, height=530)
# canvas.configure(bg=BACKGROUND_COLOR)
# image = PhotoImage(file="./images/card_back.gif")
# canvas.create_image(410,270, image = image)
# canvas.grid(column=1, row= 1)


window.mainloop()