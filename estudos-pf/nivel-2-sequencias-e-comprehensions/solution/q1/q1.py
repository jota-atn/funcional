numeros = [-1, -2, 0, 1, 2]

list_comprehension = [n * 10 for n in numeros if n > 0]

lista_map_filter = list(map(lambda n: n * 10, filter(lambda n: n > 0, numeros)))

assert list_comprehension == lista_map_filter
