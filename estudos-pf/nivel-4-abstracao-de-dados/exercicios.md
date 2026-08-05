---
title: Exercícios — Nível 4
sub_title: Abstração de Dados
theme:
  name: p1
---

# Exercícios — Nível 4: Abstração de Dados

Regras para todos os exercícios: **nada de `class`**, e nenhuma operação
pode alterar o dado recebido — sempre devolva um valor novo.

<!-- end_slide -->

## 1. TAD Fila (FIFO)

Projete o TAD `fila`, análogo à `pilha` que vimos no `README.md` deste
nível, mas com semântica **FIFO** (o primeiro que entra é o primeiro que
sai — ao contrário da pilha, que é LIFO). Implemente:

- `fila()` — construtor, cria uma fila vazia
- `eh_vazia(f)` — seletor
- `tamanho(f)` — seletor
- `enfileira(valor, f)` — devolve uma fila nova, com `valor` no fim
- `desenfileira(f)` — devolve uma tupla `(valor_removido, fila_nova)`,
  removendo o elemento mais **antigo**; se vazia, retorna `(None, f)`
- `toStr(f)` — string dos elementos, do mais antigo pro mais novo, separados por espaço

<!-- end_slide -->

Faça passar nos testes abaixo, em Python e Clojure:

```python
f1 = fila()
assert eh_vazia(f1)
assert tamanho(f1) == 0

f1 = enfileira(10, f1)
f1 = enfileira(20, f1)
f1 = enfileira(30, f1)
assert tamanho(f1) == 3
assert toStr(f1) == "10 20 30"

d, f1 = desenfileira(f1)
assert d == 10                 # sai o mais ANTIGO, diferente da pilha
assert toStr(f1) == "20 30"

# Teste de imutabilidade
f2 = fila()
f2 = enfileira(1, f2)
f2_backup = f2
f2 = enfileira(2, f2)
assert tamanho(f2_backup) == 1
assert tamanho(f2) == 2
```

<!-- end_slide -->

## 2. TAD Ponto2D

Projete o TAD `ponto` representando um ponto cartesiano `(x, y)`:

- `ponto(x, y)` — construtor
- `x(p)`, `y(p)` — seletores
- `soma_pontos(p1, p2)` — retorna um ponto novo, `(x1+x2, y1+y2)`
- `distancia_origem(p)` — retorna a distância euclidiana até `(0, 0)`

```python
p1 = ponto(3, 4)
assert x(p1) == 3
assert y(p1) == 4
assert distancia_origem(p1) == 5.0

p2 = ponto(1, 1)
p3 = soma_pontos(p1, p2)
assert x(p3) == 4
assert y(p3) == 5
# p1 não foi alterado
assert x(p1) == 3
```

<!-- end_slide -->

## 3. Pense: por que isso é um TAD válido?

Considere esta implementação alternativa de `pilha`, usando um dicionário
em vez de tupla/lista:

```python
def pilha():
    return {"itens": ()}

def empilha(valor, p):
    return {"itens": p["itens"] + (valor,)}
```

Ela ainda respeita o contrato da pilha original (mesmos testes passam)?
O que precisaria mudar em `desempilha`/`tamanho`/`toStr` para funcionar com
essa representação? Isso ilustra qual propriedade central de um TAD?

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
```python
def fila():
    return ()

def eh_vazia(f):
    return len(f) == 0

def tamanho(f):
    return len(f)

def enfileira(valor, f):
    return f + (valor,)

def desenfileira(f):
    if eh_vazia(f):
        return None, f
    return f[0], f[1:]      # remove do INÍCIO, diferente da pilha (que remove do fim)

def toStr(f):
    return " ".join(str(v) for v in f)
```

<!-- end_slide -->

```clojure
;; usar uma fila real do Clojure (clojure.lang.PersistentQueue),
;; ou simular com um vetor e remover do início

(defn fila [] clojure.lang.PersistentQueue/EMPTY)

(defn eh-vazia [f] (empty? f))

(defn tamanho [f] (count f))

(defn enfileira [valor f] (conj f valor))

(defn desenfileira [f]
  (if (eh-vazia f)
    [nil f]
    [(peek f) (pop f)]))   ;; PersistentQueue já remove do início com pop/peek

(defn to-str [f]
  (apply str (interpose " " f)))
```

<!-- end_slide -->

**2.**
```python
import math

def ponto(x, y):
    return (x, y)

def x(p):
    return p[0]

def y(p):
    return p[1]

def soma_pontos(p1, p2):
    return ponto(x(p1) + x(p2), y(p1) + y(p2))

def distancia_origem(p):
    return math.sqrt(x(p) ** 2 + y(p) ** 2)
```
```clojure
(defn ponto [x y] [x y])
(defn x [p] (nth p 0))
(defn y [p] (nth p 1))
(defn soma-pontos [p1 p2] (ponto (+ (x p1) (x p2)) (+ (y p1) (y p2))))
(defn distancia-origem [p] (Math/sqrt (+ (* (x p) (x p)) (* (y p) (y p)))))
```

<!-- end_slide -->

**3.** Sim, continua sendo um TAD válido — e essa é exatamente a questão:
o **contrato** (as funções `empilha`, `tamanho`, etc. e seu comportamento)
não muda, mesmo trocando a representação interna de tupla para dicionário.
Bastaria ajustar `tamanho`, `desempilha` e `toStr` para acessar
`p["itens"]` em vez de `p` diretamente — e nenhum código *cliente* (que só
usa `pilha()`, `empilha()`, etc.) precisaria mudar uma linha. Isso ilustra
a **barreira de abstração**: quem usa o TAD depende só do contrato, nunca
da implementação por trás.
