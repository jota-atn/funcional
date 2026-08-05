---
title: Exercícios — Nível 5
sub_title: Recursividade
theme:
  name: catppuccin-mocha
---

# Exercícios — Nível 5: Recursividade

Regra para todos os exercícios: **nenhuma solução pode usar `for` ou
`while`** — só chamadas recursivas.

<!-- end_slide -->

## 1. Identifique caso base e passo de recursão

Para cada função abaixo, aponte qual trecho é o **caso base** e qual é
o **passo de recursão**, e diga se ela é ou não uma chamada de cauda
(**tail call**).

```python
def conta(lista):
    if lista == []:
        return 0
    return 1 + conta(lista[1:])
```

```python
def conta_acc(lista, acc=0):
    if lista == []:
        return acc
    return conta_acc(lista[1:], acc + 1)
```

<!-- end_slide -->

## 2. tamanho e maximo

Implemente, **sem usar `len`/`count` nem `max`/`(apply max ...)`**, as
funções recursivas `tamanho(lista)` e `maximo(lista)` (assuma que
`lista` nunca é vazia para `maximo`), em Python e Clojure.

```python
assert tamanho([]) == 0
assert tamanho([1, 2, 3]) == 3
assert maximo([4, 9, 2, 9, 1]) == 9
assert maximo([5]) == 5
```

<!-- end_slide -->

## 3. Transforme em tail call

A função abaixo conta quantos números de `nums` são múltiplos de `k`,
mas **não** é tail call — a soma `1 + conta_multiplos(...)` é uma
operação pendente após a chamada recursiva.

```python
def conta_multiplos(nums, k):
    if nums == []:
        return 0
    resto = conta_multiplos(nums[1:], k)
    if nums[0] % k == 0:
        return 1 + resto
    return resto
```

Reescreva-a em estilo **tail call**, usando um parâmetro acumulador, em
Python. Depois, escreva a versão Clojure usando `loop`/`recur`.

```python
assert conta_multiplos([], 2) == 0
assert conta_multiplos([1, 2, 3, 4, 5, 6], 2) == 3
assert conta_multiplos([1, 2, 3, 4, 5, 6], 3) == 2
```

<!-- end_slide -->

## 4. Pense: por que fibonacci "ingênuo" não vira tail call fácil?

```python
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)
```

Tente aplicar a mesma receita do exercício 3 (introduzir um
acumulador) para transformar `fib` em tail call. O que torna esse caso
mais difícil que os anteriores? (Dica: quantas chamadas recursivas
`fib` faz por invocação, comparado com `conta_multiplos`?)

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**

Na primeira (`conta`): caso base é `if lista == []: return 0`; passo
de recursão é `return 1 + conta(lista[1:])`. **Não** é tail call —
depois que `conta(lista[1:])` retorna, ainda falta somar `1` ao
resultado; essa soma é a operação pendente.

Na segunda (`conta_acc`): caso base é `if lista == []: return acc`;
passo de recursão é `return conta_acc(lista[1:], acc + 1)`. **É** tail
call — a chamada recursiva é literalmente a última coisa que a função
faz; `acc + 1` é calculado *antes* da chamada, como argumento dela, não
depois.

<!-- end_slide -->

**2.**
```python
def tamanho(lista):
    if lista == []:
        return 0
    return 1 + tamanho(lista[1:])

def maximo(lista):
    if len(lista) == 1:
        return lista[0]
    resto_max = maximo(lista[1:])
    return lista[0] if lista[0] > resto_max else resto_max
```

<!-- end_slide -->

```clojure
(defn tamanho [lista]
  (if (empty? lista)
    0
    (+ 1 (tamanho (rest lista)))))

(defn maximo [lista]
  (if (= (count lista) 1)
    (first lista)
    (let [resto-max (maximo (rest lista))]
      (if (> (first lista) resto-max) (first lista) resto-max))))
```

<!-- end_slide -->

**3.**
```python
def conta_multiplos(nums, k, acc=0):
    if nums == []:
        return acc
    if nums[0] % k == 0:
        return conta_multiplos(nums[1:], k, acc + 1)
    return conta_multiplos(nums[1:], k, acc)
```

```clojure
(defn conta-multiplos [nums k]
  (loop [nums nums, acc 0]
    (if (empty? nums)
      acc
      (if (zero? (mod (first nums) k))
        (recur (rest nums) (inc acc))
        (recur (rest nums) acc)))))
```

Repare que a decisão "soma 1 ou não" precisou virar parte de *qual*
chamada recursiva fazer (dois `return`/`recur` possíveis), em vez de
uma operação feita depois da chamada — é assim que o `if` sai de
"depois" da recursão para "antes" dela.

<!-- end_slide -->

**4.** O problema não é a falta de acumulador — é que `fib(n)` faz
**duas** chamadas recursivas (`fib(n-1)` **e** `fib(n-2)`), e as duas
contribuem para o resultado final. Um acumulador tail-call carrega
"o que já foi calculado até agora" ao longo de **uma única** cadeia
linear de chamadas; mas aqui há duas cadeias que precisam ser
combinadas (somadas) no final, o que é exatamente a "operação
pendente" que tail call proíbe. (É possível reescrever fibonacci em
tail call, mas exige uma ideia diferente — carregar *dois*
acumuladores, um com `fib(n-1)` e outro com `fib(n-2)`, andando os
dois juntos — o que foge do escopo deste nível.)
