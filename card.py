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
        self.language = self.create_text(405, 170, text = "English", fill="white", font=("Arial", 30, "italic"))
        self.word = self.create_text(405, 280, text = "to put", fill="white", font=("Helvica", 56, "bold"))
    

    # def toogle_card(self, word):
    #     if(self.current_face) == "back":
    #         self.create_image(410,270, image = self.front)
    #         self.language = self.create_text(405, 170, text = "English", fill="black", font=("Arial", 30, "italic"))
    #         self.word = self.create_text(405, 280, text = f"{word}", fill="black", font=("Helvica", 56, "bold"))
    #         self.current_face  = "front"
    #     else:
    #         self.current_face = "back"
    #         self.create_image(410,270, image = self.back)
    #         self.language = self.create_text(405, 170, text = "French", fill="white", font=("Arial", 30, "italic"))
    #         self.word = self.create_text(405, 280, text = f"{word}", fill="white", font=("Helvica", 56, "bold"))

    def show_front(self, word):
        self.current_face  = "front"
        self.create_image(410,270, image = self.front)
        self.language = self.create_text(405, 170, text = "English", fill="black", font=("Arial", 30, "italic"))
        self.word = self.create_text(405, 280, text = f"{word}", fill="black", font=("Helvica", 56, "bold"))

    def show_back(self, word):
        self.current_face = "back"
        self.create_image(410,270, image = self.back)
        self.language = self.create_text(405, 170, text = "French", fill="white", font=("Arial", 30, "italic"))
        self.word = self.create_text(405, 280, text = f"{word}", fill="white", font=("Helvica", 56, "bold"))

    def set_word(self, word):
        self.itemconfig(self.word, text=word)
