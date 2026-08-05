---
title: Nível 1 — map, filter, reduce
sub_title: A Sagrada Trindade
theme:
  name: p1
---

# Nível 1 — map, filter, reduce (a Sagrada Trindade)

**Pré-requisito:** Nível 0 (funções puras, funções como dados de primeira classe).

**Fonte no curso:** `/srv/intro-a-loops.md`, seção "Como processar sequências?
A Sagrada Trindade!" (linhas ~116-224).

<!-- end_slide -->

## Por que "sagrada trindade"?

Praticamente todo processamento de uma coleção de dados se resume a três
operações:

<!-- incremental_lists: true -->

1. **map** — transformar cada elemento
2. **filter** — selecionar alguns elementos
3. **reduce** — agregar tudo em um único valor

<!-- incremental_lists: false -->

Se você domina essas três (e como combiná-las), você resolve a esmagadora
maioria dos problemas "dada uma lista, calcule X".

<!-- end_slide -->

## map — transformar

```python
list(map(lambda n: n ** 2, [3, 2, 8]))   # => [9, 4, 64]
```
```clojure
(map (fn [n] (* n n)) [3 2 8])  ;; => (9 4 64)
;; ou com a macro de atalho:
(map #(* % %) [3 2 8])
```

<!-- end_slide -->

## filter — selecionar

```python
list(filter(lambda n: n % 2 == 0, [1, 2, 3, 4]))   # => [2, 4]
```
```clojure
(filter even? [1 2 3 4])  ;; => (2 4)
```

Repare no `even?`/`odd?` prontos do Clojure — evitam reescrever
`(fn [n] (= (mod n 2) 0))` toda vez.

<!-- end_slide -->

## reduce — agregar

```python
from functools import reduce   # não esqueça o import!
reduce(lambda a, b: a + b, [10, 20, 30])   # => 60
```
```clojure
(reduce + [10 20 30])   ;; => 60
(reduce (fn [acc e] (+ acc e)) 0 [10 20 30])  ;; forma explícita, com valor inicial
```

<!-- pause -->

Em Python, quando a agregação é soma, `sum(...)` é mais idiomático que
`reduce` com `lambda a, b: a + b`. Reserve `reduce` pra agregações que não
têm uma função pronta (`sum`, `max`, `min`, `all`, `any`...).

<!-- end_slide -->

## Combinando as três

O padrão de `soma-pares` e `soma-cubos-impares` é sempre:
**filtra → (opcionalmente transforma) → agrega.**

```python
# soma dos cubos dos números ímpares
def soma_cubos_impares(numeros):
    impares = filter(lambda n: n % 2 != 0, numeros)
    cubos = map(lambda n: n ** 3, impares)
    return sum(cubos)
```

```clojure
(defn soma-cubos-impares [numeros]
  (reduce + 0 (map #(* % % %) (filter odd? numeros))))
```

<!-- pause -->

Repare que em Clojure a ordem de leitura é "de fora pra dentro" (reduce
de map de filter), o que fica meio invertido em relação à ordem lógica
das operações (filter, depois map, depois reduce). Isso é exatamente o
problema que o **pipelining** (Nível 3) resolve.

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei escrever `map`, `filter` e `reduce` de cabeça, em Python e
  Clojure, sem consultar nada.
- [ ] Eu sei quando usar `sum(...)` vs `reduce` em Python.
- [ ] Eu sei combinar `filter` + `map` + `reduce`/`sum` pra resolver
  "filtra, transforma e agrega".
- [ ] Eu sei usar `lambda`/`fn`/`#()` sem travar na sintaxe.

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e siga para o
**Nível 2**.
