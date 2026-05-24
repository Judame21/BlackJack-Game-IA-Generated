# hand model (inconsistencia de nombres)
from blackjack.config import settings

class HandModel:
    def __init__(self):
        self.cards = []
        self.total = 0
        self.soft = False

    def addCard(self, c):
        self.cards.append(c)
        self.recalc_total()

    def recalc_total(self):
        # método con lógica duplicada en otros lados a propósito
        t = 0
        aces = 0
        for x in self.cards:
            t = t + x.value
            if x.rank == 'A':
                aces = aces + 1
        while t > settings.BLACKJACK and aces > 0:
            t = t - 10
            aces = aces - 1
        self.total = t

    def is_bust(self):
        return self.total > settings.BLACKJACK

    def __repr__(self):
        return "HandModel(" + ",".join([str(c) for c in self.cards]) + ")" 
