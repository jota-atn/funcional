---
title: Exercícios — Nível 3
sub_title: Pipelining
theme:
  name: catppuccin-mocha
---

# Exercícios — Nível 3: Pipelining

Para todas as questões, escreva a solução como um **pipeline explícito**
(`->>` em Clojure; generator expressions encadeadas em nomes intermediários
em Python) — não use `for` com acumulador mutável.

<!-- end_slide -->

## 1. soma-notas-aprovados

`soma_notas_aprovados(turmas, N, MEDIA_MIN)` — recebe uma sequência de
turmas (cada turma é uma sequência de notas). Uma turma é "aprovada" se
tiver pelo menos `N` alunos **e** média maior ou igual a `MEDIA_MIN`.
Retorne a soma das médias das turmas aprovadas.

```python
assert soma_notas_aprovados([], 2, 6.0) == 0
assert soma_notas_aprovados([[5, 5]], 2, 6.0) == 0          # média 5.0 < 6.0
assert soma_notas_aprovados([[7, 8]], 2, 6.0) == 7.5
assert soma_notas_aprovados([[7, 8], [4]], 2, 6.0) == 7.5   # 2ª turma tem 1 aluno só
assert soma_notas_aprovados([[7, 8], [9, 10]], 2, 6.0) == 17.0
```

<!-- end_slide -->

## 2. maior-preco-com-desconto

`maior_preco_com_desconto(produtos, DESCONTO)` — recebe uma sequência de
preços. Aplique `DESCONTO` (fração, ex: `0.1` = 10%) em todos os preços
maiores que `100`, e retorne o **maior** valor resultante entre *todos* os
preços (com desconto aplicado só nos que qualificaram). Se a sequência for
vazia, retorne `0`.

```python
assert maior_preco_com_desconto([], 0.1) == 0
assert maior_preco_com_desconto([50, 80], 0.1) == 80          # nenhum > 100, sem desconto
assert maior_preco_com_desconto([50, 200], 0.1) == 180.0      # 200 * 0.9
assert maior_preco_com_desconto([300, 150], 0.5) == 150.0     # 300*0.5=150, 150*0.5=75 -> max=150
```

> Dica: pipeline aqui é `map` (aplica desconto condicional a cada preço) →
> `reduce`/`max` (pega o maior). Não precisa de `filter` separado, já que
> a condição decide *como transformar*, não *se inclui*.

<!-- end_slide -->

## 3. Encontre o bug de estilo

O código abaixo calcula o resultado certo para `soma_pares_maiores_que`,
mas **não é** um pipeline — é um `for` disfarçado. Reescreva em estilo
pipeline (Python, com generator expressions em nomes intermediários).

```python
def soma_pares_maiores_que(numeros, limite):
    resultado = 0
    for n in numeros:
        if n % 2 == 0:
            if n > limite:
                resultado = resultado + n
    return resultado
```

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
```python
def soma_notas_aprovados(turmas, N, MEDIA_MIN):
    grandes = (t for t in turmas if len(t) >= N)
    medias = (sum(t) / len(t) for t in grandes)
    aprovadas = (m for m in medias if m >= MEDIA_MIN)
    return sum(aprovadas)
```
```clojure
(defn soma-notas-aprovados [turmas N media-min]
  (->> turmas
       (filter #(>= (count %) N))
       (map #(/ (reduce + %) (count %)))
       (filter #(>= % media-min))
       (reduce + 0)))
```

<!-- end_slide -->

**2.**
```python
def maior_preco_com_desconto(produtos, desconto):
    com_desconto = (p * (1 - desconto) if p > 100 else p for p in produtos)
    return max(com_desconto, default=0)
```
```clojure
(defn maior-preco-com-desconto [produtos desconto]
  (->> produtos
       (map #(if (> % 100) (* % (- 1 desconto)) %))
       (reduce max 0)))
```

<!-- end_slide -->

**3.**
```python
def soma_pares_maiores_que(numeros, limite):
    pares = (n for n in numeros if n % 2 == 0)
    grandes = (n for n in pares if n > limite)
    return sum(grandes)
```

> Note que a lógica é idêntica à original — a diferença é inteiramente de
> **estilo**: cada etapa (filtrar pares, filtrar maiores que o limite,
> somar) agora é um passo isolado e nomeado, em vez de dois `if` aninhados
> mutando um acumulador.
