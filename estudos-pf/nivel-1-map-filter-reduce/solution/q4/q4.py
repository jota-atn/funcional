def maior_tamanho(palavras: list) -> int:
    return max(map(len, palavras))

assert maior_tamanho(["a", "bb", "ccc"]) == 3
assert maior_tamanho(["oi"]) == 2
assert maior_tamanho(["um", "dois", "tres", "quatro"]) == 6
