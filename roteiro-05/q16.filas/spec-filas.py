from filas import *

f = cria_fila()

assert eh_vazia(f) == True

enfileira(f, "primeiro")
assert eh_vazia(f) == False

enfileira(f, "segundo")
assert frente(f) == "primeiro"

valor = desenfileira(f)
assert valor == "primeiro"
assert frente(f) == "segundo"

desenfileira(f)
assert eh_vazia(f) == True

itens = [10, 20, 30]
for i in itens:
    enfileira(f, i)

assert frente(f) == 10
assert desenfileira(f) == 10
assert frente(f) == 20
