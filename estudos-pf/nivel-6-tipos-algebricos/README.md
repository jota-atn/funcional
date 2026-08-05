---
title: Nível 6 — Tipos Algébricos
sub_title: Construindo tipos por composição
theme:
  name: p1
---

# Nível 6 — Tipos Algébricos

**Pré-requisito:** Níveis 0 a 5 completos. Este nível assume que você já
pensa em funções puras e composição (Nível 3); ele dá o vocabulário
formal para isso.

**Fonte no curso:** `/srv/tipos-algebricos.md` (completo).

<!-- end_slide -->

## Reuso, em PF, é composição

Em programação funcional, o objetivo central é **reuso**, e reuso ==
**composição**: pegar funções pequenas e autocontidas e encaixá-las
como peças de Lego para formar funções maiores. Só que Lego só encaixa
se os conectores forem compatíveis — e é aí que **tipos** entram.

<!-- pause -->

Para que a composição seja sempre possível, precisamos de duas coisas:

1. **funções puras** (por definição, são composicionais — Nível 0);
2. **conectores compatíveis** — ou seja, um sistema de tipos que
   diz precisamente o que "encaixa com o quê".

<!-- end_slide -->

## O tipo de uma função

Notação matemática e sua tradução para código:

```text
f : 𝔻 → ℂ         # f tem domínio 𝔻 e contradomínio ℂ
f(d) = c          # f mapeia um valor d (de 𝔻) para c (de ℂ)
```

```python
f(d: D) -> C      # mesma coisa, em pseudo-código de programação
```

`𝔻` (domínio) é o conjunto de entradas aceitas; `ℂ`/contradomínio é o
conjunto de saídas possíveis. `𝔻 → ℂ` **é o tipo da função**.

<!-- pause -->

Exemplos: `len: str → int`; `pow: float × float → float` (dois
argumentos — o `×` aqui já antecipa o que vem no próximo slide).

<!-- end_slide -->

## Composição de funções

Dadas `f : A → B` e `g : B → C` (repare: o contradomínio de `f` **é** o
domínio de `g` — é isso que faz elas encaixarem), a composição `f ∘ g`
é a função:

```text
f ∘ g : A → C
(f ∘ g)(a) = f(g(a))
```

Leia `f ∘ g` como "*f depois de g*". Exemplo: dadas `len: str → int` e
`eh_zero: int → bool`, dá pra compor uma nova função sem escrever nada
do zero:

```python
def string_vazia(s: str) -> bool:
    return eh_zero(len(s))
# string_vazia = eh_zero ∘ len
```

Isso é literalmente o que os pipelines do Nível 3 fazem — só que lá
usávamos `->>`/generators encadeados em vez do símbolo `∘`.

<!-- end_slide -->

## Como se constroem tipos novos

Assim como compomos funções a partir de funções menores, um sistema de
tipos algébrico compõe **tipos novos a partir de tipos existentes**.
Há três operações básicas:

<!-- pause -->

- **tipos multiplicativos** (AND, "produto"): `T = U × V` — um valor de
  `T` carrega **um `U` e um `V` ao mesmo tempo**. Ex: tuplas, registros,
  dataclasses.
- **tipos aditivos** (OR, "soma"): `T = U + V` — um valor de `T` é **um
  `U` ou um `V`**, nunca os dois. Ex: `int | str`, `Option[str]`.
- **tipos recursivos**: `T = f(..., T)` — o tipo é definido em termos de
  si mesmo. Ex: uma lista.

<!-- end_slide -->

## Exemplos concretos

```text
Tipos base:    int, float, bool, str

Produtos (AND):
  tuplas:      (int, int, int)
  registros:   (nome: str, idade: int)
  dataclasses, structs, etc.

Somas (OR):
  união:       int | str                  (Python)
  Option[str]: None | Some str
  Result[int, str]: Ok int | Err str

Recursivos:
  List[int] = 1 + (int × List[int])
```

Repare que `List[int]` mistura os três: ou está vazia (`1`, um único
valor possível) ou é um `int` seguido de outra `List[int]` — soma
**e** produto **e** recursão, tudo junto.

<!-- end_slide -->

## Funções totais vs. funções parciais

Em PF, assumimos que funções são **totais**: definidas para **todo**
valor do domínio declarado. Uma função é **parcial** quando existem
valores do domínio para os quais ela não sabe o que fazer — e aí ela
tipicamente lança uma exceção. Isso é, literalmente, uma **quebra do
contrato do tipo** da função.

<!-- pause -->

Exemplo: `len: str → int` é total (funciona pra qualquer string). Já
`parse_int: str → int`, do mesmo tipo declarado, é parcial —
`parse_int("abc")` não tem resultado sensato em `int`.

<!-- end_slide -->

## Por que isso importa para PF

Lembre do Nível 0: **lançar uma exceção é um efeito colateral**, no
mesmo sentido que imprimir ou mutar uma variável externa — quebra a
transparência referencial (você não pode simplesmente substituir a
chamada pelo seu "valor", porque às vezes não há valor, há um
`throw`). Uma função parcial, então, não é realmente pura.

<!-- pause -->

Há duas formas de resolver isso, ajustando o **tipo** da função em vez
de usar `try`/`except`:

1. **restringir o domínio** — impedir que a entrada problemática chegue
   até a função;
2. **aumentar o contradomínio** — permitir que a função retorne também
   um valor que represente "deu errado" (isso é assunto do
   **Nível 7**).

<!-- end_slide -->

## Restringindo o domínio: documentação

A forma mais simples (e mais fraca) é criar um novo nome de tipo só
para documentar a intenção — sem nenhuma verificação real:

```python
type IntNaoNulo = int      # apenas um novo nome para int

def quociente(x: int, y: IntNaoNulo) -> float:
    return x / y
```

Isso **não impede** ninguém de chamar `quociente(10, 0)` — é pura
documentação. Nem em tempo de compilação, nem em tempo de execução, há
qualquer verificação.

<!-- end_slide -->

## Restringindo o domínio: verificação em tempo de execução

Para de fato impedir valores inválidos, dá pra encapsular o tipo em uma
estrutura que valida na criação:

```python
@dataclass(frozen=True)
class IntNaoNulo:
    valor: int
    def __post_init__(self):
        if self.valor == 0:
            raise TypeError("zero é valor inválido")

i1 = IntNaoNulo(5)    # ok
i2 = IntNaoNulo(0)    # erro, na criação — não no uso
```

Note o `frozen=True`: o valor, uma vez criado e validado, nunca muda —
imutabilidade de novo fazendo o trabalho pesado.

<!-- end_slide -->

## Restringindo o domínio: Design by Contract

A alternativa mais simples e direta, e a preferida da fonte deste
nível, é usar **pré-condições** no estilo *Design by Contract* (DbC):

```python
type IntNaoNulo = int

def quociente(x: int, y: IntNaoNulo) -> float:
    assert y != 0, "valor de y não pode ser zero"
    return x / y
```

Essa abordagem une a simplicidade da primeira versão à checagem em
tempo de execução da segunda, sem precisar de uma classe. O `assert`
funciona como **documentação executável** — a condição e a explicação
estão no mesmo lugar, então não podem ficar dessincronizadas.

<!-- pause -->

**Importante:** nenhuma linguagem *mainstream* (nem mesmo Haskell ou
Clojure) verifica esse tipo de restrição em tempo de **compilação** —
isso é assunto de linguagens de nicho acadêmico (Idris, Agda, F*, ...).
Na prática, `assert`/DbC (checagem em tempo de execução) é o que se
usa.

<!-- end_slide -->

## O fio que leva ao próximo nível

Restringir o domínio resolve o problema evitando que a função **veja**
a entrada inválida. Mas às vezes o valor problemático só aparece em
tempo de execução (dividir por um número que veio de um input do
usuário, por exemplo) — não dá para simplesmente proibi-lo no tipo.

Para esses casos, a solução é a outra: **aumentar o contradomínio**,
deixando a função retornar, de forma honesta e tipada, tanto o
resultado "feliz" quanto um valor representando o erro. Essa ideia —
tipos como `Result`/`Option` — é o assunto inteiro do **Nível 7**.

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei explicar o que são tipos produto (AND) e tipos soma (OR),
  com um exemplo de cada.
- [ ] Eu sei o que significa `f : A → B` e como compor duas funções
  compatíveis.
- [ ] Eu sei explicar a diferença entre função total e função parcial,
  e por que uma função parcial não é realmente pura.
- [ ] Eu sei pelo menos três formas de restringir o domínio de uma
  função para evitar exceções, e sei qual é a mais prática (DbC).

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e depois
avance para o **Nível 7** (Tratamento de Erros com Mônadas).
