---
title: Exercícios — Nível 8
sub_title: Cálculo Lambda
theme:
  name: catppuccin-mocha
---

# Exercícios — Nível 8: Cálculo Lambda

Use as definições a seguir em todos os exercícios:

```text
I = λa. a                    K  = λa. λb. a          TRUE  = λx. λy. x
M = λa. a a                  KI = λa. λb. b          FALSE = λx. λy. y
IF = λc. λt. λe. c t e       NOT = λb. b FALSE TRUE
```

Para cada expressão, reduza **passo a passo até a forma normal**,
indicando a regra usada em cada passo (α-conversão ou β-redução), como
foi feito no `README.md` deste nível.

<!-- end_slide -->

## 1. Combinadores

```text
(a) KI I M
(b) I I I
(c) K (K I) M
```

<!-- end_slide -->

## 2. Booleanos

```text
(a) NOT TRUE
(b) NOT (NOT TRUE)
(c) NOT (NOT (NOT TRUE))
```

<!-- end_slide -->

## 3. IF

```text
(a) IF TRUE M I
(b) IF FALSE M I
(c) IF (NOT TRUE) M I
```

<!-- end_slide -->

## 4. Numerais de Church

O `README.md` deste nível derivou `UM = SUC ZERO` e `DOIS = SUC UM` à
mão. Usando o mesmo método (e lembrando de fazer α-conversão nas
variáveis ligadas de `DOIS` antes de substituir, para não confundir
com as variáveis de `SUC`), derive `TRES = SUC DOIS` e confira que
bate com a definição direta `TRES = λf. λx. f (f (f x))`.

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1(a)** `KI I M`
```text
KI I M
= (λa. λb. b) I M      -- por definição de KI
= (λb. b) M             -- β-redução: a não ocorre no corpo, substituição não muda nada
= M                     -- β-redução: substitui b por M no corpo "b"
```
Forma normal: **`M`**.

<!-- end_slide -->

**1(b)** `I I I`
```text
I I I
= (λa. a) I I     -- por definição do 1º I
= I I              -- β-redução: substitui a por I no corpo "a"
= (λa. a) I        -- por definição
= I                -- β-redução
```
Forma normal: **`I`**.

<!-- end_slide -->

**1(c)** `K (K I) M`
```text
K (K I) M
= (λa. λb. a) (K I) M    -- por definição de K
= (λb. (K I)) M           -- β-redução: substitui a por (K I) no corpo "a"
= (K I)                   -- β-redução: b não ocorre no corpo, substituição não muda nada
= (λa. λb. a) I            -- por definição de K
= λb. I                    -- β-redução: substitui a por I no corpo "a"
```
Forma normal: **`λb. I`** (uma função que ignora o argumento e sempre
devolve `I`).

<!-- end_slide -->

**2(a)** `NOT TRUE`
```text
NOT TRUE
= (λb. b FALSE TRUE) TRUE     -- por definição de NOT
= TRUE FALSE TRUE              -- β-redução: substitui b por TRUE
= (λx. λy. x) FALSE TRUE       -- por definição de TRUE
= (λy. FALSE) TRUE             -- β-redução: substitui x por FALSE
= FALSE                        -- β-redução: y não ocorre no corpo
```
Forma normal: **`FALSE`**.

<!-- end_slide -->

**2(b)** `NOT (NOT TRUE)`

Já derivamos `NOT TRUE = FALSE` no item anterior. Falta `NOT FALSE`:
```text
NOT FALSE
= (λb. b FALSE TRUE) FALSE
= FALSE FALSE TRUE
= (λx. λy. y) FALSE TRUE
= (λy. y) TRUE                 -- β-redução: substitui x por FALSE, x não ocorre no corpo "y"
= TRUE                         -- β-redução: substitui y por TRUE
```
Logo `NOT (NOT TRUE) = NOT FALSE =` **`TRUE`**.

<!-- end_slide -->

**2(c)** `NOT (NOT (NOT TRUE))`

Reaproveitando os dois itens anteriores: `NOT TRUE = FALSE`,
`NOT FALSE = TRUE`, logo `NOT (NOT (NOT TRUE)) = NOT TRUE =` **`FALSE`**.
(Faz sentido: `NOT` aplicado um número ímpar de vezes inverte o valor
original uma vez líquida.)

<!-- end_slide -->

**3(a)** `IF TRUE M I`
```text
IF TRUE M I
= (λc. λt. λe. c t e) TRUE M I
= (λt. λe. TRUE t e) M I         -- β: substitui c por TRUE
= (λe. TRUE M e) I                -- β: substitui t por M
= TRUE M I                        -- β: substitui e por I
= (λx. λy. x) M I                 -- por definição de TRUE
= (λy. M) I                       -- β: substitui x por M
= M                               -- β: y não ocorre no corpo
```
Forma normal: **`M`**.

<!-- end_slide -->

**3(b)** `IF FALSE M I`

Pelo mesmo processo, `IF FALSE M I` reduz a `FALSE M I`:
```text
FALSE M I
= (λx. λy. y) M I
= (λy. y) I         -- β: substitui x por M, x não ocorre no corpo
= I                 -- β: substitui y por I
```
Forma normal: **`I`**.

<!-- end_slide -->

**3(c)** `IF (NOT TRUE) M I`

Do exercício 2(a), `NOT TRUE = FALSE`. Logo esta expressão é
equivalente a `IF FALSE M I`, que já reduzimos no item anterior.
Forma normal: **`I`**.

<!-- end_slide -->

**4.** Derivação de `TRES = SUC DOIS`.

Antes de substituir, α-convertemos as variáveis ligadas de `DOIS` (que
usa `f`, `x`, os mesmos nomes que `SUC` usa) para `f'`, `x'`, evitando
que a substituição "capture" a variável errada:

```text
DOIS ≡ λf'. λx'. f' (f' x')      -- α-conversão, mesma função
```

```text
TRES = SUC DOIS
     = (λn. λf. λx. f (n f x)) DOIS
     = λf. λx. f (DOIS f x)                         -- β: substitui n por DOIS
     = λf. λx. f ((λf'. λx'. f' (f' x')) f x)        -- desdobra DOIS (α-convertido)
     = λf. λx. f ((λx'. f (f x')) x)                  -- β: substitui f' por f
     = λf. λx. f (f (f x))                            -- β: substitui x' por x
```

Forma normal: **`λf. λx. f (f (f x))`** — exatamente a definição direta
de `TRES` dada no `README.md`. Confirma que `SUC` sozinho, aplicado
repetidamente a partir de `ZERO`, gera qualquer natural.
