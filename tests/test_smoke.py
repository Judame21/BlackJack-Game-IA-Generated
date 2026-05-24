# Tests malitos
from blackjack.services.deck_service import DeckService

def test_deck_has_cards():
    d = DeckService()
    assert len(d.cards) > 0

def test_draw_reduces():
    d = DeckService()
    n = len(d.cards)
    c = d.draw()
    assert len(d.cards) == n-1
