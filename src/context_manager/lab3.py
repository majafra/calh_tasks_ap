# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab4.py
from contextlib import contextmanager


@contextmanager
def open_db(file_name: str):
    f_obj = open(file_name)
    try:
        yield f_obj
    finally:
        f_obj.close()
