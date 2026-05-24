# Test incompleto y con cosas raras
from blackjack.models.card import Card
from blackjack.models.handModel import HandModel

def test_ace_handling_sort_of():
    h = HandModel()
    h.addCard(Card('Spades','A',11))
    h.addCard(Card('Hearts','K',10))
    assert h.total == 21

def test_bust():
    h = HandModel()
    h.addCard(Card('Spades','K',10))
    h.addCard(Card('Hearts','Q',10))
    h.addCard(Card('Clubs','2',2))
    assert h.is_bust() == True

# TODO: faltan muchos tests
