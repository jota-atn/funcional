---
title: Nível 4 — Abstração de Dados
sub_title: TADs Funcionais sem Classes
theme:
  name: catppuccin-mocha
---

# Nível 4 — Abstração de Dados sem Classes (TADs Funcionais)

**Pré-requisito:** Nível 0 (imutabilidade é o pilar central aqui).
Níveis 1-3 ajudam mas não são estritamente necessários pra este nível.

**Fonte no curso:** `/srv/slides-abstracao-de-dados-pt.md` (completo).

<!-- end_slide -->

## O que é um Tipo Abstrato de Dados (TAD)

Um TAD é definido por dois elementos:
1. um **nome** (ex: "Racional", "Pilha");
2. um **contrato**: o que os dados representam e quais operações existem
   sobre eles — sem dizer *como* são implementados por dentro.

<!-- pause -->

Quem usa o TAD só precisa conhecer o contrato. A implementação por trás
pode até mudar (de lista pra tupla, por exemplo) sem quebrar quem usa,
desde que o contrato continue valendo.

<!-- end_slide -->

## Duas categorias de operação, sempre

Ao projetar qualquer TAD, pergunte:

- **Construtores**: como eu crio um valor novo do tipo, do zero?
- **Seletores**: como eu leio/extraio informação de um valor existente?

<!-- pause -->

Exemplo do slide, para o tipo `Racional` (`p/q`):
- construtor: `racional(p, q)`
- seletores: `numer(r)`, `denom(r)`

<!-- end_slide -->

## Em PF, TAD = só funções

**Nada de `class`.** O tipo não precisa de uma "caixa" com métodos — ele
precisa de um conjunto de funções que:
1. criam valores do tipo (construtores);
2. leem valores do tipo (seletores);
3. transformam um valor do tipo em **outro valor novo** do mesmo tipo
   (operações `f: T -> T`), **nunca alterando o original.**

<!-- end_slide -->

### Construindo um exemplo do zero: o TAD Pilha

Vamos construir um exemplo do zero: o TAD **Pilha** (a estrutura clássica
"último a entrar, primeiro a sair" — como uma pilha de pratos).

**Passo 1 — o que é uma pilha?** Uma sequência de valores em que só se
acessa/remove pela "ponta de cima".

**Passo 2 — que operações preciso?** Criar uma pilha vazia, empilhar um
valor, desempilhar (remover e devolver o valor do topo), saber o tamanho,
saber se está vazia.

**Passo 3 — construtor e seletores?** `pilha()` constrói; `tamanho`,
`eh_vazia` selecionam.

<!-- end_slide -->

### Passo 4 — implementação, só com funções, sem mutação

```python
def pilha():
    return ()

def tamanho(p):
    return len(p)

def eh_vazia(p):
    return tamanho(p) == 0

def empilha(valor, p):
    return p + (valor,)   # devolve uma pilha NOVA; `p` original não muda

def desempilha(p):
    if eh_vazia(p):
        return None, p
    return p[-1], p[:-1]  # devolve (valor removido, pilha nova)
```

<!-- end_slide -->

```clojure
(defn pilha [] [])

(defn tamanho [p] (count p))

(defn eh-vazia [p] (empty? p))

(defn empilha [valor p] (conj p valor))

(defn desempilha [p]
  (if (eh-vazia p)
    [nil p]
    [(peek p) (pop p)]))
```

<!-- end_slide -->

Repare que **nenhuma** dessas funções altera o `p` que recebeu — todas
devolvem um valor novo. Isso é o que torna a implementação um TAD
funcional de verdade, e não só "uma pilha com métodos disfarçados de
funções".

<!-- pause -->

Repare também que em Clojure isso "vem de graça": as estruturas de dados
(vetor, lista, mapa) já são **persistentes** — `conj`, `pop` etc. sempre
devolvem uma versão nova sem alterar a que você tinha. Em Python você
precisa escolher estruturas que favoreçam isso (tupla em vez de lista, por
exemplo, ou sempre reatribuir o resultado de operações que "parecem"
mutar — nunca usar `.append`/`.pop` de lista, que mutam de verdade).

<!-- end_slide -->

## O contrato vira teste

O slide usa exatamente essa ideia para o tipo `Racional`:

```python
r1 = racional(1, 2)
assert numer(r1) == 1
assert denom(r1) == 2
r3 = mult(r1, racional(1, 3))
assert numer(r3) == 1
assert denom(r3) == 6
```

<!-- end_slide -->

Um conjunto de `assert`s **é** a especificação do tipo. Voltando ao
exemplo da pilha, o contrato dela pode ser escrito assim:

```python
p1 = pilha()
assert eh_vazia(p1)
assert tamanho(p1) == 0

p1 = empilha(10, p1)
p1 = empilha(20, p1)
assert not eh_vazia(p1)
assert tamanho(p1) == 2

valor, p1 = desempilha(p1)
assert valor == 20          # o último que entrou foi o primeiro a sair
assert tamanho(p1) == 1

# teste de imutabilidade: a chave de um TAD funcional
p2 = pilha()
p2 = empilha(1, p2)
p2_backup = p2
p2 = empilha(2, p2)
assert tamanho(p2_backup) == 1   # o valor antigo continua intacto
assert tamanho(p2) == 2
```

<!-- end_slide -->

Ao projetar um TAD, escrever esses testes **primeiro** ajuda a definir o
contrato antes de pensar em implementação — e o "teste de imutabilidade"
no fim é o que garante que a implementação realmente é funcional (nenhuma
operação alterou um valor que já existia).

<!-- end_slide -->

## Roteiro pra projetar qualquer TAD

<!-- incremental_lists: true -->

1. **O que é o tipo?** (definição, em português simples)
2. **Que operações preciso?** (comece pequeno, dá pra crescer depois)
3. **Quais são os construtores e seletores?**
4. **Escreva o contrato como testes** (`assert`) antes de implementar.
5. **Implemente só com funções**, garantindo que nada é mutado.

<!-- incremental_lists: false -->

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei explicar o que é um TAD e por que ele separa contrato de
  implementação.
- [ ] Eu sei identificar construtores e seletores em um tipo dado.
- [ ] Eu sei implementar um TAD imutável só com funções, em Python e
  Clojure, sem usar `class`.
- [ ] Eu sei escrever um teste que comprova que uma operação não mutou o
  dado original (como o "teste de imutabilidade" do exemplo da pilha acima).

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e depois avance
para o **Nível 5** (Recursividade).
