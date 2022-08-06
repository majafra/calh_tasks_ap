"""
Zaimplementuj dekorator klas, który automatycznie uzupełni docstringi wszystkich utworzonych metod w dekorowanej klasie.
Tekst, którym zostaną uzupełnione docstringi będzie przekazywany jako parametr do dekoratora (funkcji tworzącej dekoratory).
Nie zmieniaj docstringów metod specjalnych (takich jak __init__, czy __repr__).
"""

def deco_doc(new_docstring):
    def wrapper(obiekt):
        for atrybut in dir(obiekt):
            if not atrybut.startswith('__') and not \
                    atrybut.startswith('_') and \
                    callable(getattr(obiekt, atrybut)):
                getattr(obiekt, atrybut).__doc__ = 'They told me to write docstrings'
        return obiekt
    return wrapper

