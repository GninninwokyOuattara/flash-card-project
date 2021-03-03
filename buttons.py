from tkinter import PhotoImage, Label




class BtnRight(Label):
    def __init__(self, func):
        super().__init__()
        self.image = PhotoImage(file = "./images/right.gif")
        self.configure(image = self.image,  bg = "#B1DDC6")
        self.grid(column=1, row=1, sticky="E")
        self.bind("<Button-1>", func)



class BtnWrong(Label):
    def __init__(self, func):
        super().__init__()
        self.image = PhotoImage(file = "./images/wrong.gif")
        self.configure(image = self.image,  bg = "#B1DDC6")
        self.grid(column=1, row=1, sticky="W")
        self.bind("<Button-1>", func)