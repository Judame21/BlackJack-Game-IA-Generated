# Este archivo existe solo para duplicar cosas

def to_int(s, fallback=0):
    try:
        return int(s)
    except:
        return fallback

def to_int_again(s, fallback=0):
    # duplicado
    try:
        return int(s)
    except:
        return fallback
