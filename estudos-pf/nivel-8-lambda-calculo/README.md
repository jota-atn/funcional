---
title: Nível 8 — Cálculo Lambda
sub_title: A menor linguagem de programação possível
theme:
  name: catppuccin-mocha
---

# Nível 8 — Cálculo Lambda

**Pré-requisito:** Níveis 0 a 7 completos. Em vez de introduzir mais
uma ferramenta prática, este nível mostra o modelo teórico mínimo por
trás de tudo que você já usou: funções de primeira classe (Nível 0),
composição (Nível 6), até recursão (Nível 5).

**Fonte no curso:** `~/roteiro-10/intro-ao-calculo-lambda.md`,
`~/roteiro-10/booleans-em-lambda.md`, `~/roteiro-10/naturais-em-lambda.md`.

<!-- end_slide -->

## A menor linguagem de programação

O Cálculo Lambda é uma linguagem minimalista: só existe sintaxe e
semântica para **duas coisas** — definir funções e aplicar funções.
Nada de `if`, `for`, números, strings... nada disso é primitivo. E,
ainda assim, dá para expressar **qualquer computação possível** só com
essas duas coisas.

<!-- pause -->

> &nbsp;
> As "funções" do Cálculo Lambda são exatamente as funções que você já
> usa: funções anônimas, de primeira classe. É por isso que são
> chamadas de **lambdas** — o `lambda` do Python veio literalmente
> daqui.
> &nbsp;

<!-- end_slide -->

## A gramática inteira

```text
expr ::=   var              -- variável
       |   exp₁ exp₂        -- aplicação (invocação)
       |   λ var. exp       -- abstração (definição de função)
       |   (exp)             -- parênteses, só para legibilidade
```

Toda expressão lambda é **uma das três** (o quarto caso, parênteses, é
só açúcar sintático):

1. uma **variável**, que representa um valor ainda não definido;
2. uma **aplicação** `exp₁ exp₂` — aplicar a função `exp₁` ao valor
   `exp₂`;
3. uma **abstração** `λ var. exp` — a definição de uma função que
   recebe `var` e devolve `exp`.

<!-- pause -->

> &nbsp;
> Atenção: no Cálculo Lambda só existe **um tipo de dado — função**.
> Números, booleanos etc. (que você vai ver mais adiante neste nível)
> são só funções que, por convenção, *representam* outra coisa.
> &nbsp;

<!-- end_slide -->

## Aplicação: como se lê `f a b`

```text
f a         -- aplicação de f sobre a
f a b       -- aplicação do resultado de (f a) sobre b
(f a) b     -- o mesmo que acima (aplicação é associativa à esquerda)
f (a b)     -- aplicação de f sobre o resultado de (a b) — diferente!
```

Comparando com linguagens que você já conhece:

| Cálculo Lambda | JavaScript | Lisp / Clojure |
|---|---|---|
| `f a`     | `f(a)`    | `(f a)`   |
| `f a b`   | `f(a)(b)` | `(f a b)` |
| `f (a b)` | `f(a(b))` | `(f (a b))` |

Ou seja: `f(a)(b)` de JS — a forma **curried** de aplicar dois
argumentos, um de cada vez — é exatamente o modelo nativo do Cálculo
Lambda. Não existe "função de dois argumentos"; existe uma função que
devolve outra função.

<!-- end_slide -->

## Abstração: como se lê `λa. b`

```text
λa. b        -- função que recebe a, devolve b
λa. b c      -- função que recebe a, devolve (b c)
(λa. b) c    -- aplicação da função (λa. b) ao valor c
λa. λb. a    -- recebe a, depois recebe b, devolve a (!)
```

| Cálculo Lambda | JavaScript |
|---|---|
| `λa. b`     | `a => b` |
| `(λa. b) c` | `(a => b)(c)` |
| `λa. λb. a` | `a => b => a` |

`λa. λb. a` é a versão curried de "uma função de dois argumentos que
sempre devolve o primeiro" — um padrão que vai reaparecer logo adiante
como a definição de `TRUE`.

<!-- end_slide -->

## Semântica: como avaliar uma expressão lambda?

Avaliar uma expressão lambda é reduzi-la, passo a passo, até sua
**forma normal** (a versão mais simples possível, que não admite mais
redução) — usando duas regras.

<!-- pause -->

**β-redução** (a regra de aplicação — o "motor" da computação):
```text
(λa. E) b   =>   E[b/a]     -- substitui toda ocorrência de a por b, dentro de E
```

**α-conversão** (renomear uma variável ligada, só para evitar
confusão de nomes entre abstrações diferentes):
```text
λa. E   ≡   λb. E[b/a]
```

<!-- end_slide -->

## Exemplo passo a passo: `I I`

Seja `I = λa. a` (a função identidade).

```text
I I                     => por definição
(λa. a) (λa. a)         => α-conversão da 1ª abstração (a → b)
(λb. b) (λa. a)         => β-redução: corpo é `b`, substitui b por (λa. a)
(λa. a)                 => resultado, que é a própria definição de I
```

Ou seja: **`I I` reduz a `I`**. Faça sentido devagar: `I` aplicado a
qualquer coisa devolve essa própria coisa — inclusive quando essa
"coisa" é o próprio `I`.

<!-- end_slide -->

## Exemplo 2: `M I`, com `M = λa. a a`

```text
M I                       => pelas definições
(λa. a a) (λa. a)         => α-conversão (a → b na 1ª abstração)
(λb. b b) (λa. a)         => β-redução: substitui b por (λa. a), nas DUAS ocorrências
(λa. a) (λa. a)           => que é I I
I I                        => já vimos: reduz a I
```

Conclusão: **`M I` reduz a `I`**.

<!-- pause -->

Antes de seguir, tente derivar você mesmo `I M` (deve dar `M`, pelo
mesmo raciocínio de `I` ser identidade).

<!-- end_slide -->

## Quando não há forma normal: `M M`

```text
M M                        => pela definição de M
(λa. a a) (λa. a a)        => α-conversão
(λb. b b) (λa. a a)        => β-redução
(λa. a a) (λa. a a)        => opa — voltamos à expressão de 2 passos atrás!
...                         => loop infinito
```

`M M` **nunca** chega a uma forma normal — entra em loop para sempre.

<!-- pause -->

Isso demonstra algo importante: o Cálculo Lambda, com só essas duas
regras, já consegue expressar tanto computações que terminam quanto
computações que **não terminam** — ele tem o mesmo poder computacional
que uma Máquina de Turing.

<!-- end_slide -->

## Alguns combinadores clássicos

```text
I  = λa. a                  -- identidade
M  = λa. a a                -- mockingbird (auto-aplicação)
K  = λa. λb. a               -- kestrel: recebe dois, devolve o 1º
KI = λa. λb. b               -- (equivalente a K I): devolve o 2º
```

Guarde bem `K` e `KI` — a próxima seção (booleanos) é literalmente
esses dois combinadores com outro nome.

<!-- end_slide -->

## Booleans são seletores binários

A ideia: um booleano não precisa ser um "tipo primitivo" — pode ser
**uma função que escolhe entre duas opções**. `TRUE` sempre escolhe a
primeira; `FALSE` sempre escolhe a segunda.

```text
TRUE  = λx. λy. x     -- (isso é exatamente o K de antes!)
FALSE = λx. λy. y     -- (e isso é exatamente o KI de antes!)
```

Não é coincidência que isso pareça com como bits são implementados em
hardware (*flip-flops*) — também são, no fundo, seletores.

<!-- end_slide -->

## IF, quase de graça

Se `TRUE`/`FALSE` já **são** seletores entre duas opções, `IF` é quase
trivial — só precisa aplicar a condição às duas opções, na ordem certa:

```text
IF = λc. λt. λe. c t e
```

Se `c` é `TRUE`, `c t e` seleciona `t` (o "then"). Se `c` é `FALSE`,
`c t e` seleciona `e` (o "else"). O `IF` inteiro é só isso: **deixar a
condição, que já é uma função seletora, fazer a escolha por conta
própria**.

<!-- end_slide -->

## NOT, AND, OR

```text
NOT = λb. b FALSE TRUE
```
`NOT` usa o próprio booleano `b` para selecionar entre `FALSE` e
`TRUE` (nessa ordem invertida) — se `b` é `TRUE`, seleciona `FALSE`, e
vice-versa.

```text
AND = λa. λb. a b a
OR  = λa. λb. a a b
```

Tente ler `AND` como "se `a` for `TRUE`, o resultado é `b`; se `a` for
`FALSE`, o resultado é `a` (que já é `FALSE`)" — é exatamente a
semântica de curto-circuito do `and` que você já conhece de Python.

<!-- end_slide -->

## Números naturais: os numerais de Church

A ideia: representar o número `N` como **a função que aplica seu
primeiro argumento `N` vezes ao segundo**:

```text
ZERO  = λf. λx. x                     -- aplica f zero vezes
UM    = λf. λx. f x                   -- aplica f uma vez
DOIS  = λf. λx. f (f x)               -- aplica f duas vezes
TRES  = λf. λx. f (f (f x))           -- e assim por diante
```

De novo: essas funções não são para serem "executadas" no sentido
comum — são só uma forma de *representar* o número na memória, do
mesmo jeito que dígitos num ábaco representam quantidades.

<!-- end_slide -->

## O sucessor: gerando todos os números a partir do ZERO

Ao estilo da axiomatização de Peano (define-se `0` e uma função
"próximo número"), o Cálculo Lambda define só isso:

```text
ZERO = λf. λx. x
SUC  = λn. λf. λx. f (n f x)
```

`SUC(n)` devolve um número que aplica `f` **uma vez a mais** que `n`
aplicava — é por isso que `f (n f x)` funciona: primeiro deixa `n`
fazer suas aplicações de `f` sobre `x`, depois aplica `f` mais uma vez
sobre o resultado.

<!-- end_slide -->

## Conferindo: `SUC ZERO` é mesmo `UM`?

```text
UM = SUC ZERO                                    => pelas definições
UM = (λn. λf. λx. f (n f x)) (λf. λx. x)         => β-redução (subst. n)
UM = λf. λx. f ((λf. λx. x) f x)                 => β-redução (aplica a definição de n)
UM = λf. λx. f ((λx. x) x)                       => β-redução
UM = λf. λx. f x                                 => forma normal
```

Bateu exatamente com a definição intuitiva de `UM` que demos antes —
o que confirma que `SUC` + `ZERO` são suficientes para construir
qualquer natural, sem precisar de mais nenhuma primitiva.

<!-- end_slide -->

## Como isso se conecta com o resto da trilha

Tudo que você estudou desde o Nível 0 está, no fundo, aqui:

<!-- incremental_lists: true -->

- **funções de primeira classe** (Nível 0) — é a única coisa que
  existe no Cálculo Lambda;
- **currying** (`f a b` = `(f a) b`) — a forma nativa de aplicação,
  que Clojure/Python só imitam com múltiplos parâmetros;
- **composição** (Nível 6) — `f ∘ g`, montada só com aplicação e
  abstração;
- **recursão** (Nível 5) — mesmo sem nomear funções, dá pra expressar
  repetição (via combinadores como `M`), e algumas expressões
  simplesmente não terminam — o mesmo risco que uma função recursiva
  mal formada corre;
- **tipos como convenção, não primitiva** (Níveis 6 e 7) — booleanos e
  naturais aqui são só funções usadas de um jeito combinado; um
  `Result`/`Option` também é, no fundo, "só uma função organizada de
  um certo jeito".

<!-- incremental_lists: false -->

<!-- end_slide -->

## Checklist final

<!-- incremental_lists: true -->

- [ ] Eu sei ler e escrever expressões lambda (variável, aplicação,
  abstração), e sei que aplicação é associativa à esquerda.
- [ ] Eu sei aplicar β-redução e α-conversão para reduzir uma expressão
  passo a passo até a forma normal (ou perceber que ela não tem uma).
- [ ] Eu sei explicar por que `TRUE`/`FALSE` funcionam como seletores,
  e derivar `IF`, `NOT`, `AND`, `OR` a partir disso.
- [ ] Eu sei explicar a ideia por trás dos numerais de Church e da
  função `SUC`.

<!-- incremental_lists: false -->

Resolva `exercicios.md` para praticar reduções — é o tipo de exercício
que só melhora com repetição. Depois, avance para o **Nível 9**
(Aplicações Reais), o fechamento desta trilha.
