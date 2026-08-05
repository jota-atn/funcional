---
title: Exercícios — Nível 6
sub_title: Tipos Algébricos
theme:
  name: p1
---

# Exercícios — Nível 6: Tipos Algébricos

<!-- end_slide -->

## 1. Classifique: produto, soma ou recursivo?

Para cada tipo abaixo, diga se ele é fundamentalmente um tipo
**produto** (AND), **soma** (OR), ou **recursivo**, e explique em uma
frase por quê.

```text
(a) Pessoa = (nome: str, idade: int, email: str)
(b) Status = "pendente" | "aprovado" | "rejeitado"
(c) Arvore[int] = Folha | No(int, Arvore[int], Arvore[int])
(d) Coordenada = (x: float, y: float)
(e) Option[int] = None | Some int
```

<!-- end_slide -->

## 2. Composição de funções

Dadas as funções abaixo, com seus tipos declarados:

```text
extrai_dominio: str → str        # "user@site.com" -> "site.com"
eh_academico: str → bool         # termina em ".edu"?
```

(a) É possível compor `extrai_dominio` com `eh_academico`? Em qual
ordem? Escreva o tipo da função composta resultante.

(b) Implemente a função composta em Python, chamando-a
`email_eh_academico`, sem reescrever a lógica interna de nenhuma das
duas (use as duas funções como caixas-pretas).

<!-- end_slide -->

## 3. Total ou parcial?

Para cada função, diga se ela é **total** ou **parcial** em relação ao
tipo declarado, e, se for parcial, dê um valor do domínio que quebra o
contrato.

```python
def primeiro(lista: list) -> object:
    return lista[0]

def eh_par(n: int) -> bool:
    return n % 2 == 0

def divide_por_dois(n: float) -> float:
    return n / 2

def busca(dicionario: dict, chave: str) -> object:
    return dicionario[chave]
```

<!-- end_slide -->

## 4. Restrinja o domínio

A função abaixo é parcial: quebra se `indice` estiver fora dos limites
de `lista`.

```python
def elemento(lista: list, indice: int) -> object:
    return lista[indice]
```

Reescreva-a usando uma pré-condição em estilo **Design by Contract**
(um `assert` bem escrito, com mensagem explicativa) que documenta e
verifica a restrição, sem usar `try`/`except`.

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
- (a) Produto — um valor de `Pessoa` tem, ao mesmo tempo, um `nome` **e**
  uma `idade` **e** um `email`.
- (b) Soma — um `Status` é *um dentre* três valores possíveis, nunca uma
  combinação deles.
- (c) Recursivo (e também soma+produto por dentro, como `List`): uma
  `Arvore` é definida em termos de si mesma (`Arvore[int]` aparece na
  própria definição de `No`).
- (d) Produto — mesmo raciocínio de `Pessoa`, com dois campos.
- (e) Soma — `Option` é `None` **ou** `Some int`, nunca os dois.

<!-- end_slide -->

**2.**

(a) Sim: o contradomínio de `extrai_dominio` (`str`) é exatamente o
domínio de `eh_academico` (`str`) — os conectores encaixam. A ordem é
`eh_academico` **depois de** `extrai_dominio`:
```text
email_eh_academico : str → bool
email_eh_academico = eh_academico ∘ extrai_dominio
```

(b)
```python
def email_eh_academico(email: str) -> bool:
    return eh_academico(extrai_dominio(email))
```

<!-- end_slide -->

**3.**
- `primeiro`: **parcial**. `primeiro([])` quebra (`IndexError`) — lista
  vazia é um valor válido de `list`, mas não tem primeiro elemento.
- `eh_par`: **total**. Todo `int` tem uma resposta bem definida para
  "é par?".
- `divide_por_dois`: **total**. Diferente de uma divisão *por* uma
  variável, aqui o divisor é a constante `2` — nunca gera divisão por
  zero, então está definida para todo `float`.
- `busca`: **parcial**. `busca({}, "x")` quebra (`KeyError`) — nem toda
  `chave: str` está presente em todo `dicionario: dict`.

<!-- end_slide -->

**4.**
```python
def elemento(lista: list, indice: int) -> object:
    assert 0 <= indice < len(lista), \
        f"índice {indice} fora dos limites (tamanho {len(lista)})"
    return lista[indice]
```

Note que isso não faz `elemento` virar total "de graça" — ela continua
falhando para índices inválidos. A diferença é que agora a falha é
**documentada e explícita no ponto exato da violação**, em vez de um
`IndexError` genérico do interpretador. Pra realmente tornar a função
total (sem quebrar em nenhum caso), seria preciso a outra estratégia —
aumentar o contradomínio — que é o assunto do próximo nível.
