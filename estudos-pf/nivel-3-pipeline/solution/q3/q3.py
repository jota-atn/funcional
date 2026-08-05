def soma_pares_maiores_que(numeros: list, limite: int) -> int: 
    maiores_que_limite = (n for n in numeros if n > limite)
    pares_maiores_que_limite = (n for n in maiores_que_limite if n % 2 == 0)
    return sum(pares_maiores_que_limite)

print(soma_pares_maiores_que([1, 2, 3, 4], 2))
