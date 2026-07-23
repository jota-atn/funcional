from pilhas import *

p = cria_pilha()

assert eh_vazia(p) == True

empilha(p, 10)
assert eh_vazia(p) == False

empilha(p, 20)
assert topo(p) == 20

valor = desempilha(p)
assert valor == 20
assert topo(p) == 10

valor2 = desempilha(p)
assert valor2 == 10
assert eh_vazia(p) == True

elementos = [1, 2, 3, 4, 5]
for e in elementos:
    empilha(p, e)

assert topo(p) == 5
assert not eh_vazia(p)

