---
title: Exercícios — Nível 7
sub_title: Tratamento de Erros com Mônadas
theme:
  name: p1
---

# Exercícios — Nível 7: Tratamento de Erros com Mônadas

Para os exercícios 1 e 2, use os tipos `Ok`/`Err`/`Result` (biblioteca
`result` — `pip install result` — ou, se preferir, os equivalentes que
você mesmo vai construir no exercício 3). Em nenhum exercício use
`raise`/`try..except` para sinalizar os erros descritos no enunciado —
só `return Err(...)`.

<!-- end_slide -->

## 1. parse_idade

Implemente `parse_idade(texto)` que converte uma string para um inteiro
não-negativo (uma idade válida), retornando `Err` com uma mensagem
apropriada quando o texto não for um inteiro válido, ou quando o
inteiro for negativo.

```python
assert parse_idade("25") == Ok(25)
assert parse_idade("0") == Ok(0)
assert parse_idade("-3") == Err("idade não pode ser negativa")
assert parse_idade("abc") == Err("texto não é um inteiro válido")
```

<!-- end_slide -->

## 2. Pipeline de cadastro

Usando `parse_idade` do exercício anterior, construa um pipeline
`processa_idade(texto)` que:
1. faz o parse (exercício 1);
2. se a idade for válida mas menor que 18, converte para `Err("menor de idade")` (dica: você vai precisar de mais um `and_then`, com uma função que valida a maioridade e devolve `Ok`/`Err`);
3. se passou pelos dois passos, formata a mensagem final com `.map(...)`, produzindo a string `"cadastro liberado, idade: N"`.

```python
assert processa_idade("25").unwrap() == "cadastro liberado, idade: 25"
assert processa_idade("15").unwrap_err() == "menor de idade"
assert processa_idade("abc").unwrap_err() == "texto não é um inteiro válido"
```

<!-- end_slide -->

## 3. Implemente seu próprio Result (sem biblioteca)

Análogo ao TAD do Nível 4, mas para `Result`: implemente, **só com
funções e tuplas** (sem `class`, sem a biblioteca `result`):

- `ok(valor)` / `err(erro)` — construtores; representem o resultado
  como uma tupla `("ok", valor)` ou `("err", erro)`
- `eh_ok(r)` / `eh_err(r)` — seletores booleanos
- `valor_de(r)` — extrai o valor (de um `ok`) ou o erro (de um `err`)
- `and_then(r, f)` — se `r` for `ok`, aplica `f` ao valor de dentro
  (que deve devolver outro `ok`/`err`); se `r` for `err`, devolve `r`
  sem chamar `f`

```python
def parse(texto):
    if texto.isdigit():
        return ok(int(texto))
    return err("não é dígito")

def dobro(n):
    return ok(n * 2)

assert and_then(parse("21"), dobro) == ok(42)
assert and_then(parse("ab"), dobro) == err("não é dígito")
```

<!-- end_slide -->

## 4. Pense: pipe0.py vs. pipe1.py

Releia `/srv/monadas/pipe0.py` e `/srv/monadas/pipe1.py`. Para a
entrada `"10/0"` (divisão por zero) e para a entrada `"abc"` (formato
inválido): o que acontece em cada um dos dois programas? Em qual dos
dois é possível, olhando só a **assinatura de tipo** das funções
(`str → Result`, em vez de `str → float` com possível exceção),
prever de antemão que aquele caminho pode falhar?

<!-- end_slide -->

## Gabarito

<!-- end_slide -->

**1.**
```python
def parse_idade(texto):
    if not texto.lstrip("-").isdigit():
        return Err("texto não é um inteiro válido")
    idade = int(texto)
    if idade < 0:
        return Err("idade não pode ser negativa")
    return Ok(idade)
```

<!-- end_slide -->

**2.**
```python
def valida_maioridade(idade):
    if idade < 18:
        return Err("menor de idade")
    return Ok(idade)

def processa_idade(texto):
    return (parse_idade(texto)
            .and_then(valida_maioridade)
            .map(lambda idade: f"cadastro liberado, idade: {idade}"))
```

<!-- end_slide -->

**3.**
```python
def ok(valor):
    return ("ok", valor)

def err(erro):
    return ("err", erro)

def eh_ok(r):
    return r[0] == "ok"

def eh_err(r):
    return r[0] == "err"

def valor_de(r):
    return r[1]

def and_then(r, f):
    if eh_err(r):
        return r
    return f(valor_de(r))
```

Repare que isso é literalmente o mesmo padrão do `then`/`map` de
`pipe1.py` — só trocamos `match`/`case` sobre `Ok`/`Err` por checagem
do primeiro elemento de uma tupla. O **contrato** (o que `and_then`
promete fazer) é idêntico; só a representação interna muda — de novo,
a barreira de abstração do Nível 4.

<!-- end_slide -->

**4.** Em `pipe0.py`, as duas entradas quebram o programa com uma
exceção não tratada (`ZeroDivisionError` para `"10/0"`, e um erro de
`unpacking`/`ValueError` para `"abc"`, dependendo de onde exatamente
falha o `split`/`parse_floats`) — o programa para abruptamente, sem
chance de mostrar uma mensagem amigável. Em `pipe1.py`, as duas
entradas produzem um `Err` com mensagem específica (`"div zero"` e
`"formato inválido"`, respectivamente), e o programa continua rodando
normalmente até `unwrap_or_else` decidir o que imprimir.

Quanto à segunda pergunta: em `pipe1.py`, a assinatura de cada função
(`split_em_dois`, `parse_floats`, `divide`) já **anuncia**, olhando só
o tipo de retorno (`Result`), que aquele passo pode falhar — não
precisa ler o corpo da função pra saber. Em `pipe0.py`, a assinatura
(`float`, `tuple`, etc.) não dá nenhuma pista de que uma exceção pode
escapar dali — só descobrindo isso lendo o código, ou executando com
uma entrada ruim.
