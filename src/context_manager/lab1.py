# lab1
# Uzupełnij klase tak aby test wykorzystujący ją przeszedł poprawnie
# /tests/context_manager/test_lab1.py
# Zaimplementuj context manager za pomocą klasy

class MyContextManager:

    def __init__(self):
        print('__init')

    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__')

    def run(self):
        print('run')

if __name__ == '__main__':
    with MyContextManager() as f:
        f.run()

