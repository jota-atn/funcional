---
title: Exercícios — Nível 2
sub_title: Sequências, Comprehensions e Generators
theme:
  name: p1
---

# Exercícios — Nível 2: Sequências, Comprehensions e Generators

<!-- end_slide -->

## 1. Reescreva com comprehension

Reescreva usando list comprehension (Python) e `for` comprehension
(Clojure), em vez de `map`/`filter`:

```python
list(map(lambda n: n * 10, filter(lambda n: n > 0, numeros)))
```

<!-- end_slide -->

## 2. Reescreva com map/filter

Agora o caminho inverso — reescreva usando `map`/`filter`:

```python
[n.upper() for n in palavras if len(n) > 3]
```

<!-- end_slide -->

## 3. soma-strings-pares — com generator expression

`soma_tamanhos_pares(palavras)` — soma o **tamanho** das strings cujo
tamanho é par, usando uma **generator expression** (não list comprehension,
não `map`/`filter`).

```python
assert soma_tamanhos_pares([]) == 0
assert soma_tamanhos_pares(["a", "bb", "ccc", "dddd"]) == 6   # "bb"(2) + "dddd"(4)
assert soma_tamanhos_pares(["x", "yyy"]) == 0
```

<!-- end_slide -->

## 4. Sequência sem loop

Usando só `range`/`repeat`/comprehension (sem `for` clássico, sem `while`),
crie:

**(a)** em Python, a lista dos 10 primeiros múltiplos de 5 (começando em 5).

**(b)** em Clojure, a mesma lista.

<!-- end_slide -->

## 5. Generator de potências de 2

Escreva um generator `potencias_de_2(limite)` em Python que produz
`1, 2, 4, 8, ...` enquanto o valor for menor ou igual a `limite`.

```python
list(potencias_de_2(10))    # => [1, 2, 4, 8]
list(potencias_de_2(1))     # => [1]
list(potencias_de_2(0))     # => []
```

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
```python
[n * 10 for n in numeros if n > 0]
```
```clojure
(for [n numeros :when (pos? n)] (* n 10))
```

<!-- end_slide -->

**2.**
```python
map(lambda n: n.upper(), filter(lambda n: len(n) > 3, palavras))
```

<!-- end_slide -->

**3.**
```python
def soma_tamanhos_pares(palavras):
    return sum(len(p) for p in palavras if len(p) % 2 == 0)
```

<!-- end_slide -->

**4.**
```python
# (a)
multiplos_de_5 = [5 * n for n in range(1, 11)]
```
```clojure
;; (b)
(def multiplos-de-5 (for [n (range 1 11)] (* 5 n)))
```

<!-- end_slide -->

**5.**
```python
def potencias_de_2(limite):
    n = 1
    while n <= limite:
        yield n
        n *= 2
```

> Repare que `potencias_de_2` é preguiçoso: se você chamar
> `potencias_de_2(10**9)` e só pegar o primeiro valor com `next(...)`, ele
> não gera os outros 30 valores até que você peça.
