def cria_fila():
    return []

def eh_vazia(f):
    return len(f) == 0

def enfileira(f, elemento):
    f.append(elemento)

def frente(f):
    assert not eh_vazia(f), "Erro: Fila vazia"
    return f[0]

def desenfileira(f):
    assert not eh_vazia(f), "Erro: Fila vazia"
    return f.pop(0)
