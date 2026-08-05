from functools import reduce

def positivo(numero: int) -> bool:
    return numero > 0

def produto_positivos(sequencia: list) -> int:
    return reduce(lambda x, y: x * y, filter(positivo, sequencia), 1)

assert produto_positivos([]) == 1
assert produto_positivos([-1, -2]) == 1
assert produto_positivos([2, 3, -1]) == 6
assert produto_positivos([1, 2, 3, 4]) == 24
