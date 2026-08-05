def quadrados(numeros: list) -> list:
    return [n ** 2 for n in numeros]

def soma_quadrados_pares(sequencia: list) -> int:
    return sum(quadrados(filter(lambda n: n % 2 == 0, sequencia)))

assert soma_quadrados_pares([]) == 0
assert soma_quadrados_pares([1, 3, 5]) == 0
assert soma_quadrados_pares([1, 2, 3, 4]) == 20
assert soma_quadrados_pares([-2, 3]) == 4
