from itertools import chain
from nltk.corpus import wordnet


class JoeyApp(object):

    def __init__(self, charge, generate):
        self.charge = charge
        self.generate = generate
        self.array = []

        f = open(self.charge, 'r')
    def separate(self):
        poem = f.read()
        product = poem.split(" ")
        f.close()
        for j in range(0, len(product)):
            if product[j].isupper():
                self.words = product[j].lower()
                self.array.append(self.words)
            else:
                self.words = product[j]
                self.array.append(self.words)

    def connect(self):
        g = open(self.generate, 'w')
        for i in range(0, len(self.array)):
            synonyms = wordnet.synsets(self.array[i])
            suggestion = list(chain.from_iterable([item.lemma_names() for item in synonyms]))
            if len(suggestion) > 0:
                for j in range(0, len(suggestion)):
                    if self.array[i] != suggestion[j]:
                        element = suggestion[j].upper()
            else:
                element = self.array[i]
            g.write(element + " ")
        g.close()


if __name__ == "__main__":
    ja = JoeyApp("C:/Users/mikol/Desktop/PG/shakespeare.txt", "C:/Users/mikol/Desktop/PG/new.txt")
    ja.separate()
    ja.connect()