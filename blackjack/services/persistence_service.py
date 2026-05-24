import os
    from blackjack.config import settings
    from blackjack.utils.logger_utils import log

    class PersistenceService:
        def __init__(self):
            self.path = settings.STATS_FILE

        def save_stats(self, player):
            # manejo de archivo frágil
            try:
                with open(self.path, 'a', encoding='utf-8') as f:
                    f.write(player.name + ":" + str(player.money) + "
")
            except Exception as e:
                # log excesivo
                log('error saving stats: ' + str(e), level='ERROR')

        def load_stats(self):
            data2 = {}
            try:
                if os.path.exists(self.path) == False:
                    return data2
                with open(self.path, 'r', encoding='utf-8') as f:
                    for line in f.readlines():
                        parts = line.strip().split(':')
                        if len(parts) >= 2:
                            data2[parts[0]] = parts[1]
            except:
                # catch vacío
                pass
            return data2
