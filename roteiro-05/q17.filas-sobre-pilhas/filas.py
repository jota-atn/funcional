import pilhas

def cria_fila():
    return {
        "entrada": pilhas.cria_pilha(),
        "saida": pilhas.cria_pilha()
    }

def eh_vazia(f):
    return pilhas.eh_vazia(f["entrada"]) and pilhas.eh_vazia(f["saida"])

def enfileira(f, elemento):
    pilhas.empilha(f["entrada"], elemento)

def frente(f):
    assert not eh_vazia(f), "Erro: Fila vazia"
    if pilhas.eh_vazia(f["saida"]):
        while not pilhas.eh_vazia(f["entrada"]):
            pilhas.empilha(f["saida"], pilhas.desempilha(f["entrada"]))
    return pilhas.topo(f["saida"])

def desenfileira(f):
    assert not eh_vazia(f), "Erro: Fila vazia"
    if pilhas.eh_vazia(f["saida"]):
        while not pilhas.eh_vazia(f["entrada"]):
            pilhas.empilha(f["saida"], pilhas.desempilha(f["entrada"]))
    return pilhas.desempilha(f["saida"])
