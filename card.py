import tkinter


class Card(tkinter.Canvas):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.configure(bg="#B1DDC6", width=810, height=530, highlightthickness=0)
        self.back = tkinter.PhotoImage(file="./images/card_back.gif")
        self.front = tkinter.PhotoImage(file="./images/card_front.gif")
        self.current_face = "back"
        self.create_image(410,270, image = self.back)
        self.grid(column=0, row=0, columnspan=3)
    

    def toogle_card(self):
        if(self.current_face) == "back":
            self.create_image(410,270, image = self.front)
        else:
            self.create_image(410,270, image = self.back)
