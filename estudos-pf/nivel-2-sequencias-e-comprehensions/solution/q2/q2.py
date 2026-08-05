palavras = ["banana", "maçã", "pera"]

list_comprehension = [n.upper() for n in palavras if len(n) > 3]

lista_map_filter = list(map(str.upper, filter(lambda n: len(n) > 3, palavras)))

assert list_comprehension == lista_map_filter
print(lista_map_filter)
print(list_comprehension)
