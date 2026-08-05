---
title: Nível 3 — Pipelining
sub_title: Composição em Cadeia
theme:
  name: p1
---

# Nível 3 — Pipelining / Composição em Cadeia

**Pré-requisito:** Níveis 1 e 2 (map/filter/reduce + comprehensions).

**Fonte no curso:** não há, até agora, um slide isolado só sobre este
tema — ele aparece na prática, embutido em exercícios que combinam vários
`filter`/`map`/`reduce` em sequência. É a parte da ementa que fala em
"pipelining, threading e estilo point free".

<!-- end_slide -->

## O problema que o pipeline resolve

Quando você combina várias operações (`filter` → `filter` → `map` →
`reduce`), a leitura fica de dentro pra fora e difícil de acompanhar:

```python
sum(map(lambda seq: sum(seq) / len(seq),
        filter(lambda seq: len(seq) >= N,
               medidas)))
```

Você lê primeiro o `sum` mais externo, mas a operação que *realmente*
acontece primeiro (`filter`) está no meio do meio. Pipeline é sobre
reescrever isso pra que a ordem de leitura bata com a ordem de execução.

<!-- end_slide -->

## Clojure: `->>` (thread-last)

`->>` pega o valor inicial e vai "enfiando" ele como **último** argumento
de cada forma seguinte, uma de cada vez. Ele transforma:

```clojure
(->> medidas
     (filter #(>= (count %) N))
     (map #(/ (reduce + %) (count %)))
     (filter #(> % K))
     (reduce + 0))
```

<!-- pause -->

em, por baixo dos panos:

```clojure
(reduce + 0
  (filter #(> % K)
    (map #(/ (reduce + %) (count %))
      (filter #(>= (count %) N) medidas))))
```

<!-- pause -->

Ou seja: `->>` não muda *o que* é computado — só *como você escreve e lê*
o encadeamento. Isso é a essência de "pipelining, threading e estilo point
free": você olha o pipeline e lê, de cima pra baixo, exatamente os passos
que os dados atravessam.

<!-- end_slide -->

> Existe também `->` (thread-first), que enfia o valor como **primeiro**
> argumento em vez de último — útil quando as funções recebem o dado
> principal na primeira posição (comum em funções que manipulam mapas,
> por exemplo `assoc`, `update`). Para sequências, `->>` é o mais comum.

<!-- end_slide -->

## Python: encadear generator expressions

Python não tem um operador de pipeline nativo, mas você consegue o mesmo
efeito de legibilidade encadeando generator expressions em nomes
intermediários — sem nunca materializar uma lista completa em memória:

```python
def soma_medias_validas(medidas, N, K):
    validas = (seq for seq in medidas if len(seq) >= N)
    medias = (sum(seq) / len(seq) for seq in validas)
    medias_validas = (m for m in medias if m > K)
    return sum(medias_validas)
```

Cada nome (`validas`, `medias`, `medias_validas`) representa **um passo**
do pipeline, na ordem em que ele acontece — igual ao `->>` do Clojure, só
que sem o operador especial.

<!-- end_slide -->

## Ponto chave: nada de acumulador mutável

O que **não** é pipeline, mesmo que pareça:

```python
soma = 0
for seq in medidas:
    if len(seq) >= N:
        media = sum(seq) / len(seq)
        if media > K:
            soma += media
return soma
```

<!-- pause -->

Funciona, mas é o estilo imperativo do Nível 0 disfarçado dentro de uma
função — variável `soma` mutando passo a passo, lógica de filtro e
agregação misturadas em um só bloco. O pipeline separa cada responsabilidade
(filtrar por tamanho, calcular média, filtrar por valor, somar) em uma
etapa isolada e nomeada.

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei ler e escrever um pipeline `->>` em Clojure com 3+ etapas.
- [ ] Eu sei montar o equivalente em Python usando generator expressions
  encadeadas em nomes intermediários.
- [ ] Eu sei explicar por que um `for` com acumulador mutável **não** é a
  mesma coisa que um pipeline, mesmo calculando o resultado certo.

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e siga para o
**Nível 4**.
