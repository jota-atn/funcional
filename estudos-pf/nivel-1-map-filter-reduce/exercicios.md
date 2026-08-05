---
title: Exercícios — Nível 1
sub_title: map, filter, reduce
theme:
  name: catppuccin-mocha
---

# Exercícios — Nível 1: map, filter, reduce

Escreva cada função em Python **e** em Clojure, usando `map`/`filter`/
`reduce` (evite `for` clássico e mutação). Os testes usam `assert` — rode
seu código e veja se todas as linhas passam sem erro.

<!-- end_slide -->

## 1. soma-multiplos-de-3

`soma_multiplos_de_3(numeros)` — soma os números da sequência que são
múltiplos de 3.

```python
assert soma_multiplos_de_3([]) == 0
assert soma_multiplos_de_3([1, 2, 4, 5]) == 0
assert soma_multiplos_de_3([3, 6, 9]) == 18
assert soma_multiplos_de_3([1, 3, 5, 9]) == 12
assert soma_multiplos_de_3([-3, 3]) == 0
```

<!-- end_slide -->

## 2. conta-negativos

`conta_negativos(numeros)` — conta quantos números da sequência são
negativos (dica: `map` que transforma cada número em `1` ou `0`, e depois
soma — ou use `filter` e `len`/`count`).

```python
assert conta_negativos([]) == 0
assert conta_negativos([1, 2, 3]) == 0
assert conta_negativos([-1, -2, 3]) == 2
assert conta_negativos([0, -5]) == 1
```

<!-- end_slide -->

## 3. soma-quadrados-pares

`soma_quadrados_pares(numeros)` — soma os **quadrados** dos números
**pares** da sequência (repare: filtra antes de elevar ao quadrado).

```python
assert soma_quadrados_pares([]) == 0
assert soma_quadrados_pares([1, 3, 5]) == 0
assert soma_quadrados_pares([1, 2, 3, 4]) == 20   # 2² + 4² = 4 + 16
assert soma_quadrados_pares([-2, 3]) == 4
```

<!-- end_slide -->

## 4. maior-tamanho

`maior_tamanho(palavras)` — recebe uma sequência de strings e retorna o
tamanho da maior delas, usando `reduce` (dica: a função de combinação
recebe dois tamanhos parciais e devolve o maior; ou combine `map` com
`max` como "reduce pronto").

```python
assert maior_tamanho(["a", "bb", "ccc"]) == 3
assert maior_tamanho(["oi"]) == 2
assert maior_tamanho(["um", "dois", "tres", "quatro"]) == 6
```

<!-- end_slide -->

## 5. produto-positivos

`produto_positivos(numeros)` — multiplica todos os números positivos da
sequência entre si. Se não houver nenhum, retorna `1` (elemento neutro da
multiplicação — por isso o valor inicial do `reduce` importa aqui).

```python
assert produto_positivos([]) == 1
assert produto_positivos([-1, -2]) == 1
assert produto_positivos([2, 3, -1]) == 6
assert produto_positivos([1, 2, 3, 4]) == 24
```

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
```python
def soma_multiplos_de_3(numeros):
    return sum(filter(lambda n: n % 3 == 0, numeros))
```
```clojure
(defn soma-multiplos-de-3 [numeros]
  (reduce + 0 (filter #(zero? (mod % 3)) numeros)))
```

<!-- end_slide -->

**2.**
```python
def conta_negativos(numeros):
    return len(list(filter(lambda n: n < 0, numeros)))
```
```clojure
(defn conta-negativos [numeros]
  (count (filter neg? numeros)))
```

<!-- end_slide -->

**3.**
```python
def soma_quadrados_pares(numeros):
    pares = filter(lambda n: n % 2 == 0, numeros)
    return sum(map(lambda n: n ** 2, pares))
```
```clojure
(defn soma-quadrados-pares [numeros]
  (reduce + 0 (map #(* % %) (filter even? numeros))))
```

<!-- end_slide -->

**4.**
```python
from functools import reduce

def maior_tamanho(palavras):
    tamanhos = map(len, palavras)
    return reduce(lambda a, b: a if a > b else b, tamanhos)
```
> `max(map(len, palavras))` também é válido e mais idiomático em Python —
> `max` é, na prática, um `reduce` especializado.
```clojure
(defn maior-tamanho [palavras]
  (reduce max (map count palavras)))
```

<!-- end_slide -->

**5.**
```python
from functools import reduce

def produto_positivos(numeros):
    positivos = filter(lambda n: n > 0, numeros)
    return reduce(lambda a, b: a * b, positivos, 1)
```
```clojure
(defn produto-positivos [numeros]
  (reduce * 1 (filter pos? numeros)))
```

> Repare que tanto em Python (`reduce(f, seq, 1)`) quanto em Clojure
> (`reduce f 1 seq`) dá pra passar um **valor inicial** — essencial quando
> a sequência filtrada pode ficar vazia (soma → inicial `0`; produto →
> inicial `1`).
