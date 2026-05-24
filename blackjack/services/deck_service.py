import random
from blackjack.models.card import Card
from blackjack.utils.logger_utils import log

class DeckService:
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        suits = ['Hearts','Diamonds','Clubs','Spades']
        ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10,'A':11}
        self.cards = []
        for s in suits:
            for r in ranks:
                self.cards.append(Card(s, r, values[r]))
        random.shuffle(self.cards)  # random no cripto-seguro (hotspot)
        log('Deck built with ' + str(len(self.cards)) + ' cards')

    def draw(self):
        if len(self.cards) == 0:
            self.build()
        return self.cards.pop(0)

    def draw2(self):
        # duplicado
        if len(self.cards) == 0:
            self.build()
        return self.cards.pop(0)
