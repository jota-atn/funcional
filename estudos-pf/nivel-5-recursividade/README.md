---
title: Nível 5 — Recursividade
sub_title: Repetição sem laços, sem atribuições
theme:
  name: catppuccin-mocha
---

# Nível 5 — Recursividade

**Pré-requisito:** Níveis 0 a 4 completos (mentalidade funcional é a base
central deste nível: recursão só faz sentido de verdade quando você já
está confortável com imutabilidade e funções puras).

**Fonte no curso:** `/srv/intro-a-recursao.md` (completo).

<!-- end_slide -->

## O que é recursividade

Recursividade é o nome dado a descrições de processos que fazem
referência ao próprio processo que estão descrevendo. Em termos de
programação: é uma forma de produzir repetição usando **apenas
definições de funções**, sem `for`/`while`.

<!-- pause -->

Isso não é um detalhe estilístico. Lembre do Nível 0: programação
funcional evita atribuição mutável. Um laço `for`/`while` clássico
*precisa* de uma variável que muda a cada volta (`soma += x`, `i += 1`).
Recursão resolve o mesmo problema sem nenhuma variável mutável — cada
"passo" é uma chamada de função nova, com seus próprios argumentos.

<!-- end_slide -->

## A forma geral de toda função recursiva

Toda função recursiva bem formada tem, no mínimo, duas partes:

1. **caso base** (ou caso de parada) — não faz chamada recursiva;
2. **passo de recursão** — faz a chamada recursiva, sobre uma entrada
   "menor" que caminha em direção ao caso base.

<!-- pause -->

O passo de recursão **precisa** convergir para o caso base — senão você
tem uma recursão infinita (o equivalente recursivo de um `while True`
sem `break`).

<!-- end_slide -->

## Exemplo 1: fatorial

Definição matemática:

```
              ⎧ 1,                se n = 0
fatorial(n) = ⎨
              ⎩ n × fatorial(n-1), caso contrário
```

A tradução para código segue quase literalmente a definição matemática:

```python
def fatorial(n):
    if n == 0:
        return 1
    return n * fatorial(n - 1)
```

```clojure
(defn fatorial [n]
  (if (= n 0)
    1
    (* n (fatorial (dec n)))))
```

<!-- end_slide -->

## Exemplo 2: soma de uma sequência

Compare as duas versões abaixo. A primeira é a forma "com laço",
imperativa — repare nas duas variáveis **mutáveis** (`soma` e `num`):

```python
def soma(nums):
    soma = 0
    for num in nums:
        soma += num
    return soma
```

<!-- pause -->

A especificação matemática, análoga à do fatorial:

```
             ⎧ 0,                        se nums == []
soma(nums) = ⎨
             ⎩ nums[0] + soma(nums[1:]), caso contrário
```

<!-- end_slide -->

E a implementação que segue direto da especificação:

```python
def soma(nums):
    if nums == []:
        return 0
    return nums[0] + soma(nums[1:])
```

```clojure
(defn soma [nums]
  (if (empty? nums)
    0
    (+ (first nums) (soma (rest nums)))))
```

Nenhuma variável muda de valor. `nums[1:]` (ou `(rest nums)`) cria uma
visão nova, menor, da sequência a cada chamada — a soma final só é
montada "na volta" de cada chamada recursiva.

<!-- pause -->

Detalhe de performance: em Python, `nums[1:]` é O(n) (copia a lista). Em
Clojure, `(rest nums)` é O(1) — as estruturas de dados de Clojure são
projetadas para recursão desse tipo.

<!-- end_slide -->

## Por que recursão, e não laços?

A recursão não é um capricho estético de linguagens funcionais — ela
nasce do esforço da matemática, no início do século 20, para formalizar
os próprios fundamentos do raciocínio matemático, **antes de existir
computador**. Dois princípios guiavam esse esforço:

<!-- pause -->

1. **imutabilidade não é negociável**: se um nome está associado a um
   valor, não há por que essa associação mudar — isso só gera confusão
   no raciocínio;
2. **minimalismo**: quanto menos construções básicas, mais fácil
   provar coisas sobre a linguagem. Se dá pra expressar repetição
   ajustando a própria noção de função (referenciando-a a si mesma),
   não há motivo pra inventar um comando de laço à parte.

<!-- end_slide -->

No discurso de recebimento do prêmio Turing (1977), John Backus
argumentou que a **atribuição** (no sentido de *redefinir* o valor de
um nome já existente) é o que prende as linguagens de programação a um
modelo de máquina baseado em mutação de memória. Programação funcional
é, nesse sentido, **programar sem atribuições** — e recursão é a
consequência natural dessa restrição: é como você repete algo quando
não pode reatribuir uma variável.

<!-- end_slide -->

## Tail call (recursão de cauda)

`fatorial` e `soma`, como escritas acima, têm algo em comum: depois que
a chamada recursiva retorna, ainda falta fazer uma operação (a
multiplicação, a soma). Isso significa que o interpretador precisa
**guardar** o estado de cada chamada (em uma pilha) até a chamada mais
interna retornar.

<!-- pause -->

> &nbsp;
> Quando o código de uma função **não** deixa nenhuma operação pendente
> para depois da chamada recursiva — ou seja, a chamada recursiva é
> literalmente a última coisa que a função faz — dizemos que é uma
> chamada de cauda (**tail call**).
> &nbsp;

<!-- end_slide -->

## Exemplo 3: fatorial em versão tail call

```python
def fatorial(n, acc=1):
    if n == 0:
        return acc
    return fatorial(n - 1, n * acc)
```

Aqui a multiplicação `n * acc` acontece **antes** da chamada recursiva
(vira argumento dela) — não sobra nada pendente depois que a chamada
recursiva retorna. Linguagens que otimizam isso (*tail call
optimization*, TCO) reaproveitam o mesmo espaço de pilha a cada chamada
— na prática, a recursão de cauda roda com o mesmo custo de espaço de
um `while`.

<!-- end_slide -->

## Como transformar uma função em tail call

**Estratégia 1 — a partir da versão recursiva convencional**: identifique
a operação pendente e introduza um parâmetro acumulador que já vai
carregando o resultado parcial.

```
f(n)      = operacao(n, f(n - 1))          -- não é tail call
f(n, acc) = f(n - 1, operacao(n, acc))     -- é tail call
```

<!-- pause -->

**Estratégia 2 — a partir de um `while True` puro**: escreva a versão
com laço de forma que haja um único `return`/`break` dentro de um
`while True`; as variáveis do laço viram os parâmetros extras da função
recursiva (incluindo o próprio acumulador).

```python
def funcao(args, acc=<inicial>):
    if <condicao_parada>:
        return acc
    return funcao(<args_atualizados>, <acc_atualizado>)
```

<!-- end_slide -->

## Clojure: `loop`..`recur`

Em Clojure, recursão de cauda **não é garantida automaticamente**
mesmo quando a função chama a si mesma na última posição — a JVM não
otimiza isso por padrão. Por isso Clojure tem uma sintaxe própria,
`loop`/`recur`, que **força** e **garante** TCO:

```clojure
(defn fatorial
  ([n] (fatorial n 1N))
  ([n acc]
    (if (= n 0)
      acc
      (recur (dec n) (* n acc)))))
```

`recur` só pode aparecer na posição de cauda — o compilador recusa o
código se não for o caso. Isso troca "confiar que o compilador otimiza"
por "o compilador garante, ou nem compila".

<!-- end_slide -->

## Quando tail call não basta: thunks e trampolins

Mesmo com uma função escrita em estilo tail call, se a linguagem **não
faz** TCO (é o caso de Python), a pilha ainda estoura para entradas
grandes. A solução, nesse caso, é um **trampolim**.

<!-- pause -->

Um **thunk** é uma função sem argumentos que só *adia* uma computação:

```python
thunk = lambda: fatorial(n - 1, n * acc)   # não executa ainda
valor = thunk()                             # executa agora
```

Um **trampolim** é um laço que fica executando thunks até obter um
valor que não seja mais um thunk:

```python
def trampolim(f):
    while callable(f):
        f = f()
    return f
```

<!-- end_slide -->

Juntando as peças: a função recursiva, em vez de chamar a si mesma
diretamente, **retorna um thunk** que fará a chamada — quem realmente
invoca a próxima chamada é o `trampolim`, fora da pilha de chamadas da
função original:

```python
def fatorial(n, acc=1):
    if n == 0:
        return acc
    return lambda: fatorial(n - 1, n * acc)

print(trampolim(fatorial(1500)))   # não estoura a pilha
```

Isso é, na prática, um "hack" para simular TCO em linguagens que não a
oferecem nativamente — mas resolve o problema de verdade.

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei identificar caso base e passo de recursão em uma função
  dada.
- [ ] Eu sei escrever uma função recursiva simples a partir de sua
  especificação matemática, em Python e Clojure.
- [ ] Eu sei explicar por que uma função é (ou não é) tail call.
- [ ] Eu sei transformar uma função recursiva convencional em uma
  versão tail call, usando um parâmetro acumulador.
- [ ] Eu sei o que `loop`/`recur` garante em Clojure, e por que isso é
  diferente de recursão simples.
- [ ] Eu entendo, ao menos conceitualmente, o papel de thunks e
  trampolins.

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e depois
avance para o **Nível 6** (Tipos Algébricos).
