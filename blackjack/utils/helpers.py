# helpers
import os, re, json

def ugly_input(prompt, default=""):
    try:
        x = input(prompt)
        if x is None or x == "":
            return default
        return x
    except Exception:
        # manejo incorrecto
        return default

def to_int(s, fallback=0):
    try:
        return int(s)
    except:
        return fallback

def insecure_eval_math(expr):
    # Security hotspot: eval
    # Intento (pobre) de limitar a operaciones matemáticas básicas
    if expr is None:
        return 0
    ok = True
    for ch in expr:
        if ch not in "0123456789+-*/() ":
            ok = False
    if ok == True:
        try:
            return eval(expr)
        except Exception:
            return 0
    return 0

def read_json_loose(path):
    # sin validación; path puede venir de cualquier lado
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except:
        return {}

def write_json_loose(path, obj):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(json.dumps(obj))
    except:
        pass

# código muerto
def never_used_function():
    tmp = 1
    tmp = tmp + 1
    return tmp

# Comentado sin eliminar
# def old_helper():
#     print('old')
