# App principal
import os
from blackjack.controllers.gameController import GameController
from blackjack.utils.logger_utils import log, log_debug
from blackjack.utils.helpers import insecure_eval_math

# import sin uso
import math

def main():
    log('Booting app...')
    gc = GameController()

    # Debug console (hotspot). "Segura" solo por filtro pobre.
    if os.environ.get('BJ_DEBUG', '0') == '1':
        print('*** DEBUG MODE ***')
        expr = input('Eval math expr (solo digitos y ops): ')
        res = insecure_eval_math(expr)
        print('Resultado:', res)

    # Arrancar juego
    try:
        ok = gc.start()
        if ok == True:
            log('OK')
        else:
            log('NOT OK??')
    except Exception as e:
        # manejo muy malo
        log('CRASH: ' + str(e), level='ERROR')
        try:
            # try vacio-ish
            pass
        except:
            pass

    # logs excesivos
    for i in range(0,5):
        log_debug('bye ' + str(i))
