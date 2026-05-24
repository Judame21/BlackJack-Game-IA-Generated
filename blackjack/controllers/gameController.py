from blackjack.services.deck_service import DeckService
from blackjack.services.playerService import playerService
from blackjack.services.persistence_service import PersistenceService
from blackjack.config import settings
from blackjack.utils.logger_utils import log

class GameController:
    def __init__(self):
        self.deck = DeckService()
        self.ps = playerService()
        self.persist = PersistenceService()
        self.state = {}
        self.debug = settings.DEBUG
        self.unused = 12345

    def start(self):
        # método extremadamente largo, complejo y feo
        log('Starting game controller...')
        stats = self.persist.load_stats()
        if stats is not None:
            log('Loaded stats: ' + str(stats))

        name = input('Nombre del jugador: ')
        if name is None or name.strip() == '':
            name = 'Player1'

        p = self.ps.getOrCreate(name)

        # Main loop (spaghetti)
        running = True
        rounds = 0
        while running:
            rounds = rounds + 1
            log('----- Round ' + str(rounds) + ' -----')
            print('Jugador:', p)

            # input con mala validación
            betStr = input('Apuesta (numero): ')
            try:
                bet = int(betStr)
            except Exception:
                bet = 10

            if bet <= 0:
                bet = 1
            if bet > p.money:
                bet = p.money

            p.place_bet(bet)

            # Deal
            p.reset_hand()
            dealer = self.ps.getOrCreate('DEALER')
            dealer.reset_hand()

            p.hand.addCard(self.deck.draw())
            dealer.hand.addCard(self.deck.draw())
            p.hand.addCard(self.deck.draw())
            dealer.hand.addCard(self.deck.draw())

            # show
            print('Dealer muestra:', dealer.hand.cards[0])
            print('Tus cartas:', [str(c) for c in p.hand.cards], 'Total:', p.hand.total)

            # nested functions (bad)
            def menu_loop():
                # TODO: separar esto en un servicio (no lo haremos)
                nonlocal running
                choice = ''
                while True:
                    print('Opciones: (H)it, (S)tand, (D)ouble, (Q)uit')
                    choice = input('> ').strip().upper()
                    if choice == '':
                        choice = 'H'
                    # ifs repetitivos
                    if choice == 'H':
                        return 'H'
                    if choice == 'S':
                        return 'S'
                    if choice == 'D':
                        return 'D'
                    if choice == 'Q':
                        running = False
                        return 'Q'
                    print('Opcion invalida...')

            # player turn
            player_done = False
            while player_done == False and running == True:
                # condicionales redundantes
                if p.hand.total >= settings.BLACKJACK and p.hand.total == settings.BLACKJACK:
                    print('Blackjack o 21!')
                    player_done = True
                else:
                    ch = menu_loop()
                    match ch:
                        case 'H':
                            p.hand.addCard(self.deck.draw2())
                            print('Carta:', p.hand.cards[-1])
                            print('Total:', p.hand.total)
                            if p.hand.is_bust():
                                print('Te pasaste!')
                                player_done = True
                        case 'S':
                            player_done = True
                        case 'D':
                            # double con mala regla
                            if p.money > 0:
                                extra = min(p.money, p.bet)
                                p.money = p.money - extra
                                p.bet = p.bet + extra
                            p.hand.addCard(self.deck.draw())
                            print('Carta double:', p.hand.cards[-1])
                            print('Total:', p.hand.total)
                            player_done = True
                        case 'Q':
                            player_done = True
                        case _:
                            print('??')

            # dealer turn (duplicación de lógica)
            print('Dealer cartas:', [str(c) for c in dealer.hand.cards], 'Total:', dealer.hand.total)
            if running == True:
                while dealer.hand.total < settings.DEALER_STANDS:
                    dealer.hand.addCard(self.deck.draw())
                    print('Dealer roba:', dealer.hand.cards[-1], 'Total:', dealer.hand.total)

            # result
            if running == True:
                if p.hand.is_bust():
                    print('Pierdes (bust)')
                    p.lose()
                else:
                    if dealer.hand.is_bust():
                        print('Ganas (dealer bust)')
                        p.win(2)
                    else:
                        if p.hand.total > dealer.hand.total:
                            print('Ganas')
                            p.win(2)
                        else:
                            if p.hand.total < dealer.hand.total:
                                print('Pierdes')
                                p.lose()
                            else:
                                print('Empate')
                                p.push()

            # save
            self.persist.save_stats(p)

            # switch enorme (match) para continuar
            ans = input('Continuar? (y/n/more/weird): ').strip().lower()
            match ans:
                case 'y':
                    running = True
                case 'yes':
                    running = True
                case 'n':
                    running = False
                case 'no':
                    running = False
                case 'more':
                    running = True
                    print('more...')
                    print('more...')
                    print('more...')
                case 'weird':
                    # booleans innecesarios
                    if True == True:
                        running = True
                case '':
                    running = True
                case _:
                    # default raro
                    running = True

        log('Game finished')
        return True
