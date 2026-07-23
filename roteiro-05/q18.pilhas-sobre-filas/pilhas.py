import filas

def cria_pilha():
    return filas.cria_fila()

def eh_vazia(p):
    return filas.eh_vazia(p)

def empilha(p, elemento):
    filas.enfileira(p, elemento)

def topo(p):
    assert not eh_vazia(p), "Erro: Pilha vazia"
    
    tamanho = 0
    aux = filas.cria_fila()
    while not filas.eh_vazia(p):
        item = filas.desenfileira(p)
        filas.enfileira(aux, item)
        tamanho += 1
    
    ultimo = None
    for i in range(tamanho):
        ultimo = filas.desenfileira(aux)
        filas.enfileira(p, ultimo)
        
    return ultimo

def desempilha(p):
    assert not eh_vazia(p), "Erro: Pilha vazia"
    
    tamanho = 0
    aux = filas.cria_fila()
    while not filas.eh_vazia(p):
        filas.enfileira(aux, filas.desenfileira(p))
        tamanho += 1
    
    for i in range(tamanho - 1):
        filas.enfileira(p, filas.desenfileira(aux))
    
    return filas.desenfileira(aux)
