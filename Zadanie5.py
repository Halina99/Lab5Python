class Liczba:
    def __init__(self, liczba):
        self.liczba = liczba

    def __add__(self, other):
        return self.liczba**2 + 2*self.liczba*other.liczba + other.liczba**2


x = Liczba(2)
y = Liczba(3)

print(x + y)
