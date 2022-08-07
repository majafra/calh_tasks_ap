# lab4
# Napisz manager contextu wspierający operacje na bazie danych w naszym przypadku sqllite
# https://docs.python.org/3/library/sqlite3.html
# /tests/context_manager/test_lab4.py
import sqlite3
from contextlib import contextmanager

@contextmanager
def open_db(file_name: str):
    connection = sqlite3.connect(file_name)
    try:
        cursor = connection.cursor()
        print("Database created and Successfully Connected to SQLite")
        yield cursor
        cursor.close()
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)
    finally:
        connection.close()

# try:
#     sqliteConnection = sqlite3.connect('SQLite_Python.db')
#     cursor = sqliteConnection.cursor()
#     print("Database created and Successfully Connected to SQLite")
#
#     sqlite_select_Query = "select sqlite_version();"
#     cursor.execute(sqlite_select_Query)
#     record = cursor.fetchall()
#     print("SQLite Database Version is: ", record)
#     cursor.close()
#
# except sqlite3.Error as error:
#     print("Error while connecting to sqlite", error)
# finally:
#     if sqliteConnection:
#         sqliteConnection.close()
#         print("The SQLite connection is closed")