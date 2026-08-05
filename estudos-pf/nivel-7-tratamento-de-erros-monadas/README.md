---
title: Nível 7 — Tratamento de Erros com Mônadas
sub_title: Result, Ok, Err e o padrão que resolve tudo isso
theme:
  name: catppuccin-mocha
---

# Nível 7 — Tratamento de Erros com Mônadas

**Pré-requisito:** Níveis 0 a 6 completos. Este nível continua
diretamente de onde o Nível 6 parou: "aumentar o contradomínio" para
evitar exceções.

**Fonte no curso:** `/srv/intro-a-monadas.md` e a segunda metade de
`/srv/tipos-algebricos.md`; estudo de caso em `/srv/monadas/pipe0.py`
e `/srv/monadas/pipe1.py`.

<!-- end_slide -->

## Erros não são exceções

A Programação Funcional separa duas coisas que `try`/`except` costuma
misturar:

<!-- pause -->

**Erros** — falhas incontornáveis do ambiente (sem memória, disco
cheio, banco de dados fora do ar). Não há o que "tratar" além de parar
graciosamente.

**Exceções** — situações fora do "caminho feliz" mas totalmente
esperadas e administráveis pela lógica da aplicação (dividir por zero,
string vazia, índice fora dos limites).

<!-- end_slide -->

> &nbsp;
> O problema, do ponto de vista da Programação Funcional: `try..catch`
> usa **o mesmo mecanismo de linguagem** para as duas coisas. Erros são
> falha de ambiente e pedem parada controlada. Exceções são parte da
> especificação da função, e merecem ser tratadas como **saída normal**
> — não como um desvio escondido do fluxo principal.
> &nbsp;

Este nível trata do segundo caso: como expressar "essa função pode não
ter uma resposta feliz" **no tipo de retorno**, em vez de com `raise`.

<!-- end_slide -->

## Relembrando o Nível 6: as duas soluções

Uma função `f: D → C` é parcial quando existem valores em `D` para os
quais ela não tem resposta. No nível anterior vimos a solução
"restringir `D`". A outra solução é **aumentar `C`**:

```text
f : ℤ × ℤ → ℝ              -- quociente, declarado como total, mas parcial na prática
f : ℤ × ℤ → (ℝ ∪ 𝔼)        -- ajustado: C agora inclui um tipo de erro 𝔼
```

Com isso, os casos especiais voltam a usar `return`, e não `raise` — a
saída "deu errado" é só mais um valor possível do contradomínio, não
uma porta dos fundos.

<!-- end_slide -->

## Passo 1: união de tipos simples

```python
def quociente(x: int, y: int) -> float | str:
    if y == 0:
        return "y deve ser diferente de zero"
    return x / y

res = quociente(10, 0)
if type(res) is str:
    print(f"erro: {res}")
else:
    print(res)
```

Funciona, mas o código cliente precisa testar `type(res)` manualmente
toda vez — não há nada que **force** quem chama `quociente` a lidar com
o caso de erro.

<!-- end_slide -->

## Passo 2: pattern matching

```python
def quociente(x: int, y: int) -> float | str:
    if y == 0:
        return "y deve ser diferente de zero"
    return x / y

res = quociente(10, 0)
match res:
    case str(erro):
        print(f"erro: {erro}")
    case int(valor):
        print(valor)
```

Melhor — mas ainda é fácil confundir "um `str` de erro" com "um `str`
que por acaso é o resultado feliz de outra função".

<!-- end_slide -->

## Passo 3: os tipos Ok, Err e Result

A solução final é criar **tipos dedicados** para "deu certo" e "deu
errado", que não se confundem com nenhum outro tipo de dado:

```python
from result import Ok, Err, Result

def quociente(x: int, y: int) -> Result:
    if y == 0:
        return Err("y deve ser diferente de zero")
    return Ok(x / y)

res = quociente(10, 1)
match res:
    case Err(erro):
        print(f"erro: {erro}")
    case Ok(valor):
        print(valor)
```

`Ok` e `Err` "empacotam" um dado numa caixa que diz se é o caminho
feliz ou não; `Result` é a união dos dois tipos — em termos do Nível 6,
`Result = Ok + Err`, um tipo soma.

<!-- end_slide -->

## Isso é uma mônada

Pense em um `Result` como uma **caixa** que guarda ou um valor, ou um
erro. Uma **mônada**, nesse sentido prático (esqueça a bagagem
matemática do nome), é exatamente esse padrão: um tipo "caixa" com um
jeito padronizado de **encadear operações** sobre o valor de dentro,
sem precisar abrir a caixa a cada passo para checar se deu erro.

<!-- pause -->

O encadeamento vem do método `.and_then(f)`: aplica `f` ao valor de
dentro da caixa **se** for um `Ok`, e simplesmente propaga o `Err`
adiante sem chamar `f`, se for um `Err`.

<!-- end_slide -->

## Pipeline com Result

```python
res = Ok(dado_inicial)
res = res.and_then(funcao1)
res = res.and_then(funcao2)
res = res.and_then(funcao3)
print(res)   # Ok(valor) ou Err(erro) — nunca uma exceção não tratada
```

Se `funcao1` retornar `Err`, `funcao2` e `funcao3` **nunca são
chamadas** — o erro atravessa o resto do pipeline sozinho. É a mesma
vantagem dos pipelines do Nível 3 (`->>`), com o bônus de propagação de
erro embutida.

<!-- end_slide -->

## Exemplo completo

```python
def parse_int(valor: str) -> Result[int, str]:
    try:
        return Ok(int(valor))
    except ValueError:
        return Err("valor inválido como int")

def calcula_raiz(valor: int) -> Result[float, str]:
    if valor < 0:
        return Err("valor não pode ser negativo")
    return Ok(math.sqrt(valor))

def processe(value: str) -> Result[float, str]:
    return parse_int(value).and_then(calcula_raiz)

processe("16")   # Ok(4.0)
processe("-4")   # Err("valor não pode ser negativo")
processe("abc")  # Err("valor inválido como int")
```

Repare: o único `try/except` que sobra é para converter uma exceção
*real* da biblioteca padrão (`int("abc")`) numa saída honesta do tipo
`Result` — a fronteira entre "mundo com exceções" e "mundo funcional"
fica isolada num único lugar.

<!-- end_slide -->

## O método `.map()`: quando `f` não devolve um Result

`.and_then(f)` espera que `f` já devolva um `Result`. Se você quiser
encadear uma função "comum", que devolve um valor cru:

```python
def dobro(n: int) -> int:
    return 2 * n

def processe(value: str) -> Result[float, str]:
    return (parse_int(value)
           .map(dobro)              # dobro NÃO devolve Result
           .and_then(calcula_raiz)) # calcula_raiz devolve Result
```

`.map(f)` desempacota o valor, aplica `f`, e **empacota de novo** o
resultado num `Ok` — assim `f` nem precisa saber que `Result` existe.

<!-- end_slide -->

## Desempacotando no final: `.unwrap()`, `.ok()`, `.unwrap_err()`

```python
v1 = processe("16")    # Ok(4.0)
v2 = processe("-4")    # Err("valor não pode ser negativo")

v1.unwrap()             # 4.0
v1.ok()                  # 4.0
v2.ok()                  # None
v2.unwrap_err()          # "valor não pode ser negativo"
```

Você usa esses métodos **só no final** do pipeline, quando finalmente
precisa decidir o que fazer com o resultado (imprimir, salvar,
mostrar erro na tela). Ao longo do pipeline, o valor fica sempre
"empacotado" — ninguém precisa checar tipo a cada passo.

<!-- end_slide -->

## Estudo de caso: refatorando um pipeline real

`/srv/monadas/pipe0.py` lê uma linha tipo `"10/2"`, separa, converte
para `float` e divide — sem nenhum tratamento de erro real, só `print`s
de depuração espalhados pelo meio:

```python
def divide(par):
    num, den = par
    return num / den

def parse_floats(par):
    str1, str2 = par
    return float(str1), float(str2)

def split_em_dois(linha):
    return linha.split("/")

# no main(): dado = split_em_dois(dado); print(...)
#            dado = parse_floats(dado);  print(...)
#            dado = divide(dado);        print(...)
```

Se a entrada for `"abc"` ou `"10/0"`, o programa simplesmente quebra
com uma exceção não tratada.

<!-- end_slide -->

`/srv/monadas/pipe1.py` reescreve exatamente o mesmo pipeline usando
`Result`. Repare que as três funções de domínio agora **retornam
`Ok`/`Err` em vez de levantar exceção**:

```python
def divide(par):
    num, den = par
    if den == 0: return Err("div zero")
    return Ok(num / den)

def parse_floats(par):
    try:
        str1, str2 = par
        return Ok((float(str1), float(str2)))
    except:
        return Err("floats inválidos")

def split_em_dois(linha: str):
    if linha.count("/") != 1:
        return Err("formato inválido")
    return Ok(linha.split("/"))
```

<!-- end_slide -->

E o pipeline no `main()` vira uma cadeia legível, sem nenhum `if` de
verificação de erro no meio:

```python
dado = (Ok(valor)
        .and_then(split_em_dois)
        .and_then(parse_floats)
        .and_then(divide)
        .map(quadrado))

quociente = dado.unwrap_or_else(lambda e: f"o erro foi: {e}")
print(quociente)
```

Nenhum estágio precisa saber se um estágio anterior falhou — `Err` se
propaga sozinho até o fim, onde `unwrap_or_else` decide o que mostrar.

<!-- end_slide -->

## Bônus: implementando seu próprio `.and_then`/`.map`

`pipe1.py` também mostra que, se você não quiser depender da biblioteca
`result`, dá pra implementar o mecanismo à mão — e ele não é mágico,
é só duas funções de alta ordem que fazem *pattern matching*:

```python
def then(f):
    def f_adaptada(caixa):
        match caixa:
            case Ok(valor): return f(valor)
            case Err(erro): return Err(erro)
    return f_adaptada

def map(f):
    def f_adaptada(caixa):
        match caixa:
            case Ok(valor): return Ok(f(valor))
            case Err(erro): return Err(erro)
    return f_adaptada
```

Isso é exatamente o espírito do Nível 4: um TAD (`Result`), com um
contrato bem definido, implementado sem segredo nenhum por trás.

<!-- end_slide -->

## Promises também são mônadas

O mesmo padrão aparece em JavaScript: uma `Promise` é uma "caixa" que
guarda o resultado (eventual) de uma operação assíncrona, e que expõe
`.then(f1, f2)` para encadear o que fazer se ela resolver ou rejeitar.
Cada `.then()` devolve uma nova `Promise` — o mesmo mecanismo de
encadeamento de `Result`, só que para "ainda não tenho o valor" em vez
de "posso ter dado errado".

<!-- end_slide -->

## Checklist antes de avançar

<!-- incremental_lists: true -->

- [ ] Eu sei explicar a diferença entre erro e exceção, na visão da PF.
- [ ] Eu sei por que `raise`/`try..catch` quebra pureza e transparência
  referencial.
- [ ] Eu sei o que `Ok`, `Err` e `Result` representam, e por que
  `Result` é um tipo soma.
- [ ] Eu sei encadear operações com `.and_then()` e `.map()`, e sei
  quando usar cada um.
- [ ] Eu sei desempacotar um `Result` no final de um pipeline.

<!-- incremental_lists: false -->

Se todos os itens estão marcados, resolva `exercicios.md` e depois
avance para o **Nível 8** (Cálculo Lambda).
