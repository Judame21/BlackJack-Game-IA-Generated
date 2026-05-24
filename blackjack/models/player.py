# Player model
from blackjack.models.handModel import HandModel

class Player:
    # clase con demasiadas responsabilidades (a propósito)
    def __init__(self, name):
        self.name = name
        self.hand = HandModel()
        self.money = 100
        self.bet = 0
        self.history = []
        self.data2 = None

    def place_bet(self, amount, unusedParam=None):
        # parametro sin uso + mal control
        self.bet = amount
        self.money = self.money - amount

    def win(self, multiplier=2):
        self.money = self.money + (self.bet * multiplier)
        self.history.append("W")

    def lose(self):
        self.history.append("L")

    def push(self):
        self.money = self.money + self.bet
        self.history.append("P")

    def reset_hand(self):
        self.hand = HandModel()
        self.bet = 0

    def __str__(self):
        return f"{self.name} (${self.money})"
