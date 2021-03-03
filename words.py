import pandas, random

class Words():
    def random_index(self):
        idx = random.randint(0, len(self.df)-1)
        if not idx in self.knowed_index:
            self.index = idx
        else: 
            self.random_index()

    def __init__(self):
        self.df = pandas.read_csv("./data/french_words.csv")
        self.knowed_index = []
        self.index = None
        self.random_index()
        # self.french_word = self.dataframe["French"][self.index]
        # self.english_word = self.dataframe["English"][self.index]




        