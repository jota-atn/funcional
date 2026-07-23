def cria_pilha():
    return []

def eh_vazia(p):
    return len(p) == 0

def empilha(p, elemento):
    p.append(elemento)

def topo(p):
    assert not eh_vazia(p), "Erro: Pilha vazia"
    return p[-1]

def desempilha(p):
    assert not eh_vazia(p), "Erro: Pilha vazia"
    return p.pop()
