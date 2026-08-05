def eh_negativo(numero: int) -> bool:
    return 1 if numero < 0 else 0 

def negativos(sequencia: list) -> list:
    return map(eh_negativo, sequencia)

def conta_negativos(sequencia: list) -> int:
    return sum(negativos(sequencia))

assert conta_negativos([]) == 0
assert conta_negativos([1, 2, 3]) == 0
assert conta_negativos([-1, -2, -3]) == 3
assert conta_negativos([0, -5]) == 1
