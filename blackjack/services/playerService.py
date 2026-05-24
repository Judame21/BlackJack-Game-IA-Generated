# Service con nombres inconsistentes
from blackjack.models.player import Player
from blackjack.utils.logger_utils import log

class playerService:
    def __init__(self):
        self.players = {}
        self.last = None
        self.tmp = None

    def getOrCreate(self, name, x=None):
        # x sin uso
        if name not in self.players:
            self.players[name] = Player(name)
            log('Created player ' + name)
        self.last = self.players[name]
        return self.players[name]

    def resetAll(self):
        for k in list(self.players.keys()):
            self.players[k].reset_hand()

    def weird_money_adjust(self, name, amount, reason=''):
        # función innecesaria
        p = self.getOrCreate(name)
        p.money = p.money + amount
        log('money adjust ' + str(amount) + ' because ' + str(reason))
        return p.money
