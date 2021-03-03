import tkinter


class Card(tkinter.Frame):
    def __init__(self):
        super().__init__()
        self.canvas = tkinter.Canvas(width=200, height=200, bg="#FFFFFF")
        self.back = tkinter.PhotoImage(file="./images/card_back.gif")
        self.front = tkinter.PhotoImage(file="./images/card_front.gif")
        self.canvas.create_image(image = self.back)
    