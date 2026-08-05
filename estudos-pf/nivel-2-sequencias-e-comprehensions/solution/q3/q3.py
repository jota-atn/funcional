def soma_tamanhos_pares(sequencia: list) -> int:
    return sum(len(n) for n in sequencia if len(n) % 2 == 0)

assert soma_tamanhos_pares([]) == 0
assert soma_tamanhos_pares(["a", "bb", "ccc", "dddd"]) == 6
assert soma_tamanhos_pares(["x", "yyy"]) == 0
