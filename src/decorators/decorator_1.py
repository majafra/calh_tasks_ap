"""
Zaimplementuj dekorator, który sprawdzi, czy dekorowana funkcja ma zdefiniowane typingi (dla zmiennych oraz zwracanego obiektu)
Jeżeli brak jakiegokolwiek typingu, to udekorowana funkcja przy próbie wywołania nie powinna się wykonać,
powinna natomiast zwrócić string, z komunikatem:
"add typings to function <nazwa_funkcji>, please!"
gdzie nazwa_funkcji jest nazwą dekorowanej funkcji.
"""
from functools import wraps


def require_typing(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            if fn.__annotations__['a'] and fn.__annotations__['b'] and fn.__annotations__['return']:
                result = fn(*args, **kwargs)
                return result
        except:
            return f'add typings to function {fn.__name__}, please!'
    return wrapper








