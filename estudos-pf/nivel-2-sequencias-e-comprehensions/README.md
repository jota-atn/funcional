---
title: Nível 2 — Sequências e Comprehensions
sub_title: Comprehensions e Generators
theme:
  name: p1
---

# Nível 2 — Sequências, Comprehensions e Generators

**Pré-requisito:** Nível 1 (map/filter/reduce).

**Fonte no curso:** `/srv/intro-a-loops.md` (criação de sequências:
`range`, `repeat`, list comprehension, `for` do Clojure — linhas ~54-113)
e `/srv/slides-pt-aula-07.md` (generators com `yield`).

<!-- end_slide -->

## Duas formas de dizer a mesma coisa

`map`/`filter` e comprehensions resolvem o mesmo problema com sintaxes
diferentes. Você vai encontrar as duas formas em código real — vale a
pena reconhecer e escrever ambas com fluência.

```python
# com map/filter
list(map(lambda n: n ** 3, filter(lambda n: n % 2 != 0, numeros)))

# com list comprehension — mesma coisa, mais legível
[n ** 3 for n in numeros if n % 2 != 0]
```

<!-- pause -->

Em Clojure, o equivalente à comprehension é o `for`:

```clojure
(for [n numeros :when (odd? n)] (* n n n))
```

**Atenção**, e isso é repetido no material: o `for` de Clojure **não é**
um laço imperativo. É uma comprehension — uma expressão que produz uma
sequência nova, igual ao `for` do Python dentro de colchetes.

<!-- end_slide -->

## List comprehension vs. generator expression (Python)

```python
quadrados_lista = [n ** 2 for n in range(1000000)]   # cria a lista inteira na memória, JÁ
quadrados_gen   = (n ** 2 for n in range(1000000))   # cria um objeto "preguiçoso"
```

A troca de `[...]` por `(...)` faz Python calcular **sob demanda**, um
elemento de cada vez, em vez de materializar tudo de uma vez na memória.
Combinada com `sum`/`max`/`any`, essa é a forma mais idiomática de
filtrar-e-agregar em uma linha só:

```python
sum(l**3 for l in lista if l % 2 == 1)
```

Aqui `sum` consome o generator item a item — nunca existe uma lista
intermediária.

<!-- end_slide -->

## Sequências "prontas" (sem loop nenhum)

```python
range(1, 6)      # 1, 2, 3, 4, 5 — sob demanda
4 * [0]          # [0, 0, 0, 0]
```
```clojure
(range 1 6)      ;; (1 2 3 4 5)
(repeat 4 0)     ;; (0 0 0 0)
```

<!-- end_slide -->

## Generators com `yield` (Python)

Um generator é uma função que, em vez de `return`, usa `yield` — cada
`yield` "pausa" a função e devolve um valor; na próxima iteração ela
retoma de onde parou.

```python
def contagem_regressiva(ini):
    n = ini
    while True:
        yield n
        n -= 1
        if n < 0:
            break

for v in contagem_regressiva(3):
    print(v)   # 3, 2, 1, 0
```

<!-- pause -->

Isso é uma **sequência preguiçosa (lazy)**: os valores só são calculados
conforme são consumidos, o que permite, por exemplo, representar sequências
infinitas sem estourar memória.

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei converter entre `map`/`filter` e list/generator comprehension,
  nos dois sentidos.
- [ ] Eu sei explicar a diferença prática entre `[...]` e `(...)` em Python.
- [ ] Eu sei que o `for` do Clojure é uma comprehension, não um laço.
- [ ] Eu sei escrever uma função generator simples com `yield`.

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e siga para o
**Nível 3**.
