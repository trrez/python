from . import card
import random


class Deck:

    def __init__(self):
        self.cards = []

        for i in range(1, 14):
            if i == 1:
                i = 1 or 10
            elif i == 11:
                i = 10
            elif i == 12:
                i = 10
            elif i == 13:
                i = 10
            else:
                i
            self.cards.append(card.Card(i))

    def show_cards(self):
        for card in self.cards:
            card_aleatoria = random.randint(self.cards)
            print(card_aleatoria)

    def handle(self):
        while (self.cards != 18):
            for card in self.cards:
                card.show_cards()
