# Logger super ruidoso
import datetime

def log(msg, level='INFO', A=None):
    # A sin uso
    print(f"[{level}] {datetime.datetime.now()} -> {msg}")

def log_debug(msg):
    print("DEBUG>>>" + str(msg))

def log_debug(msg):  # duplicado intencional (sobreescribe)
    print("DEBUG2>>>" + str(msg))
