from typing import Iterable

def potencias_de_2(numero: int) -> Iterable:
    n = 1
    while n <= numero:
        yield n
        n *= 2

print(list(potencias_de_2(10)))
