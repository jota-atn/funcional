---
title: Nível 0 — Mentalidade Funcional
sub_title: Estudos de Programação Funcional
theme:
  name: p1
---

# Nível 0 — Mentalidade Funcional

**Pré-requisito:** nenhum. Este é o chão da casa.

**Fonte no curso:** `/srv/intro-a-loops.md` (seção "Programação Funcional X
Loops Imperativos", linhas ~22-113) e ideias repetidas em
`/srv/slides-abstracao-de-dados-pt.md`.

<!-- end_slide -->

## O que muda de verdade

Programar em estilo funcional não é "usar `map` em vez de `for`". É mudar
a pergunta que você faz sobre o código.

| Estilo Imperativo | Estilo Funcional |
|---|---|
| "Como eu construo esse resultado, passo a passo?" | "O que esse resultado *é*, em termos de outros dados?" |
| Comandos executados em sequência | Expressões avaliadas |
| Variáveis mudam de valor (mutação) | Nomes são amarrados a um valor, ponto final |
| Loops com variável de controle | Sequências transformadas por funções |

<!-- end_slide -->

## Os quatro pilares

### 1. Computação como avaliação de expressões

```python
# imperativo: "receita" de como chegar no resultado
pares = []
for n in range(6):
    if n % 2 == 0:
        pares.append(n)
```

<!-- pause -->

```python
# funcional: o resultado É uma expressão
pares = [n for n in range(6) if n % 2 == 0]
```

A segunda versão não descreve *passos*. Ela descreve *o que a lista é*.

<!-- end_slide -->

### 2. Imutabilidade

Depois de criado, um dado nunca é alterado. Se você "precisa mudar algo",
você cria um **novo** valor com a mudança e descarta (ou guarda em outro
nome) o antigo.

```python
lista_original = [1, 2, 3]
lista_nova = lista_original + [4]   # cria uma lista NOVA

print(lista_original)   # [1, 2, 3] — intacta
print(lista_nova)       # [1, 2, 3, 4]
```

<!-- pause -->

Compare com a versão mutante, que a PF evita:

```python
lista_original = [1, 2, 3]
lista_original.append(4)   # ALTERA a lista existente
# agora não existe mais como era antes — qualquer outra parte do código
# que guardou uma referência a `lista_original` também "vê" a mudança
```

Esse detalhe parece pequeno, mas é a raiz de uma classe inteira de bugs
difíceis de rastrear: uma função altera um dado que outra parte do
programa não esperava que mudasse, porque as duas partes seguravam a
"mesma" lista.

<!-- end_slide -->

### 3. Funções puras

Uma função é pura quando:
- **é determinística**: mesma entrada, sempre a mesma saída;
- **não tem efeito colateral**: não altera nada fora dela (variável global,
  arquivo, print, argumento mutável recebido por referência).

```python
def dobro(n):        # pura
    return n * 2

total = 0
def acumula(n):       # IMPURA: depende de e altera `total`, que é externo
    global total
    total += n
    return total
```

<!-- end_slide -->

### 4. Transparência referencial

Consequência direta de pureza: se `f(x)` é referencialmente transparente,
você pode **substituir a chamada `f(x)` pelo seu valor de retorno** em
qualquer lugar do código sem mudar o comportamento do programa. Isso é o
que permite ao compilador/você raciocinar sobre um pedaço de código
isoladamente, sem rastrear o "estado" do programa inteiro.

```python
def quadrado(n):
    return n * n

y = quadrado(3) + quadrado(3)
# é sempre equivalente a:
y = 9 + 9
# porque quadrado(3) sempre vale 9, sem exceção
```

Um `input()` ou um `random()` no meio da função quebram isso: o valor de
retorno passa a depender de "quando" ou de "quanto" a função é chamada, não
só dos argumentos.

<!-- end_slide -->

## Funções como dados de primeira classe

Em PF, funções são valores como qualquer outro: podem ser guardadas em
variáveis, passadas como argumento e retornadas por outras funções.

```python
def aplica_duas_vezes(f, x):
    return f(f(x))

aplica_duas_vezes(lambda n: n + 3, 10)  # => 16
```

```clojure
(defn aplica-duas-vezes [f x]
  (f (f x)))

(aplica-duas-vezes #(+ % 3) 10) ;; => 16
```

Essa propriedade é o que torna `map`, `filter` e `reduce` (nível 1)
possíveis: eles são funções que **recebem outras funções** como argumento.

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei explicar, com minhas palavras, a diferença entre um `for`
  clássico e uma list comprehension.
- [ ] Eu sei dizer se uma função dada é pura ou não, e por quê.
- [ ] Eu entendo por que imutabilidade impede um tipo de bug clássico
  (alguém altera um dado que outra parte do código ainda espera intacto).
- [ ] Eu sei escrever uma função que recebe outra função como argumento.

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` deste nível e
siga para o **Nível 1**.
