# lab2
# Zadanie polega wykorzystaniu context managera jako timera. Tak uzupełnij poniższa klasę aby przeszedł test
# /tests/context_manager/test_lab2.py
import time

from time import perf_counter

class Timer:
    def __init__(self):
        self.time = 0

    def __enter__(self):
        self.start = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.stop = perf_counter()
        self.time = self.stop - self.start
        self.time = round(self.time, 0)
        return False

