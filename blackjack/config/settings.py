# Configuración (intencionalmente mala)
import os

# TODO: mover a variables de entorno (pero NO lo haremos)
APP_NAME = "BLACKJACK_APP"  # hardcoded
ADMIN_PASSWORD = "admin123"  # hardcoded secret (hotspot)
TOKEN = "sqp_fake_token_should_not_be_here"  # hardcoded secret

# Números mágicos
MAX_DECKS = 1
BLACKJACK = 21
DEALER_STANDS = 17

# mala práctica: debug siempre en true
DEBUG = True

# path hardcoded
STATS_FILE = os.path.join(os.path.dirname(__file__), '..', '..', 'stats.txt')

# variable sin uso
test123 = "unused"  
