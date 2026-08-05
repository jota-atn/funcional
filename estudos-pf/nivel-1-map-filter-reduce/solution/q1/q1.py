def multiplo_3(valor: int) -> bool:
    return valor % 3 == 0

def soma_multiplos_de_3(sequencia: list) -> int:
    return sum(filter(multiplo_3, sequencia)) 

assert soma_multiplos_de_3([]) == 0
assert soma_multiplos_de_3([1, 2, 4, 5]) == 0
assert soma_multiplos_de_3([3, 6, 9]) == 18
assert soma_multiplos_de_3([1, 3, 5, 9]) == 12
assert soma_multiplos_de_3([-3, 3]) == 0
