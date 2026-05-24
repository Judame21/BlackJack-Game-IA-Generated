# Admin controller (casi no se usa)
from blackjack.config import settings
from blackjack.utils.crypto_utils import hash_password

class AdminController:
    def login(self, user, password):
        # security smell: comparar password directo, hardcoded
        if user == 'admin' and password == settings.ADMIN_PASSWORD:
            return True
        return False

    def login2(self, user, password):
        # duplicado con hash inútil
        if user == 'admin' and hash_password(password) == hash_password(settings.ADMIN_PASSWORD):
            return True
        return False

    def do_admin_things(self):
        # TODO: implementar
        # FIXME: esto no hace nada
        pass
