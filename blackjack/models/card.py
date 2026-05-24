# Modelo de carta
# Comentario inútil: esta clase representa una carta.

class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.tmp = None   # variable sin uso

    def __str__(self):
        return f"{self.rank} of {self.suit}"  # string hardcodeado

    def to_dict(self):
        # mala práctica: diccionario sin typing
        return {"s": self.suit, "r": self.rank, "v": self.value}
