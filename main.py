BACKGROUND_COLOR = "#B1DDC6"

from card import Card
from tkinter import Tk, Canvas, PhotoImage

window  = Tk()
window.title("Flash Card")
window.config(padx=50, pady=20)
window.configure(bg=BACKGROUND_COLOR)
window.grid_columnconfigure(0, weight = 1,minsize=20)
window.grid_columnconfigure(1, weight = 1, minsize = 300)
window.grid_columnconfigure(2, weight = 1,minsize=20)
# card = Card()
# card.pack()
canvas = Canvas(width=810, height=530)
canvas.configure(bg=BACKGROUND_COLOR)
image = PhotoImage(file="./images/card_back.gif")
canvas.create_image(410,270, image = image)
canvas.grid(column=1, row= 1)


window.mainloop()