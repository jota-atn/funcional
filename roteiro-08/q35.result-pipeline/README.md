# Exercício: Pipeline de notificações com `Result` em Rust

## Objetivo

Praticar o tratamento monádico de erros em Rust usando `Result<T,
E>` com o operador `?`, compondo funções que podem falhar em um
pipeline.

## Contexto

Assim como o `Optional` em Java e o pacote `result` em Python,
Rust oferece `Result<T, E>` para operações que podem ter sucesso
(`Ok(T)`) ou falhar (`Err(E)`). Diferentemente de exceções, o
`Result` é um tipo **valor** — não há mecanismo oculto de
propagação; o programador decide explicitamente como lidar com
cada erro.

Rust oferece duas formas de compor `Result`s:

1. **Operador `?`** — propaga o erro automaticamente para quem
   chamou a função (equivalente a um `return Err(e)` prematuro).
   É a forma mais idiomática.
2. **Métodos funcionais** — `map`, `and_then`, `or_else`,
   `unwrap_or`, etc. (análogos ao `Optional` em Java).

> Diferente de Java e até de Python ou Javascript, em Rust, Ok e
> Err são parte da biblioteca padrão e do ferramental padrão para
> se lidar com a linguagem. Mais que isso a cultura de
> programação em Rust usa tratamento monádico de erros com tipos
> monádicos, functores e tipos algébricos/abstratos de dados,
> além de vários outros elementos de programação funcional.

## O que fazer

Implemente as quatro funções abaixo em `src/main.rs`:

### `find_user(id: u32) -> Result<&'static User, String>`

Busca um usuário pelo ID no array estático `USERS`. Retorna
`Err("Usuário {id} não encontrado")` se o ID não existir.

### `get_email(user: &User) -> Result<&'static str, String>`

Extrai o email do usuário. Retorna `Err("{nome} não possui
email")` se o email for `None`.

### `notify_user(id: u32) -> Result<String, String>`

Compõe `find_user` + `get_email` usando o operador `?`. Retorna:
- `Ok("Enviando email para {nome} em <{email}>")` em caso de sucesso
- O `Err` da primeira função que falhar (propagado via `?`)

### `notify_multiple(ids: &[u32]) -> Vec<String>`

Processa uma lista de IDs e coleta apenas as notificações
bem-sucedidas. Use iteradores com `filter_map(Result::ok)` — sem
laços explícitos.

## Dados

O banco de usuários estático contém:

| ID | Nome | Email                |
|----|-------|---------------------|
| 1  | Alice | `alice@example.com` |
| 2  | Bob   | `None`              |
| 3  | Carol | `carol@test.com`    |

## Exemplos de comportamento

| Chamada                            | Resultado                                                                                               |
|------------------------------------|---------------------------------------------------------------------------------------------------------|
| `find_user(1)`                     | `Ok(&User("Alice", ...))`                                                                               |
| `find_user(99)`                    | `Err("Usuário 99 não encontrado")`                                                                      |
| `get_email(bob)`                   | `Err("Bob não possui email")`                                                                           |
| `notify_user(1)`                   | `Ok("Enviando email para Alice em <alice@example.com>")`                                                |
| `notify_user(2)`                   | `Err("Bob não possui email")`                                                                           |
| `notify_multiple(&[1, 2, 3, 99])`  | `["Enviando email para Alice em <alice@example.com>", "Enviando email para Carol em <carol@test.com>"]` |
| `notify_multiple(&[2, 99])`        | `[]`                                                                                                    |

## Compilando e executando

```bash
cargo test    # Executa os testes
```

## Comparação entre linguagens

Você já usou monads de erro em outras linguagens neste mesmo tema
(email de usuário). Aqui está uma comparação conceitual — com
exemplos *fora* do domínio do exercício para não entregar a resposta.

### Java — `Optional.map().orElse()`

```java
// parse de um inteiro a partir de uma string
Optional<Integer> idade = Optional.ofNullable(input)
    .map(Integer::parseInt)
    .filter(i -> i >= 0)
    .orElse(0);
```

`Optional` representa **ausência de valor**. Não carrega informação
sobre *por que* o valor está ausente.

### Python — pacote `result`

```python
# leitura de um arquivo cujo conteúdo pode ser inválido
def ler_config(caminho: str) -> Result[str, str]:
    try:
        with open(caminho) as f:
            return Ok(f.read())
    except FileNotFoundError:
        return Error("Arquivo não encontrado")

config = (ler_config("config.txt")
          .map(lambda s: s.strip())
          .unwrap_or("default"))
```

`Result` (assim como o `Either` funcional) carrega **informação de erro**
no caso de falha — análogo ao `Result` do Rust.

### Rust

Rust oferece duas formas de compor `Result`s:

```rust
// Exemplo com outro tema: divisão segura
fn dividir(a: f64, b: f64) -> Result<f64, String> {
    if b == 0.0 {
        Err("Divisão por zero".to_string())
    } else {
        Ok(a / b)
    }
}

// Operador ?  —  propaga o erro automaticamente
fn calcular( x: f64) -> Result<f64, String> {
    let r1 = dividir(10.0, x)?;
    let r2 = dividir(r1, 2.0)?;
    Ok(r2)
}

// Estilo funcional  —  and_then (equivalente ao flatMap)
fn calcular_and_then(x: f64) -> Result<f64, String> {
    dividir(10.0, x)
        .and_then(|r| dividir(r, 2.0))
}
```

O operador `?` é syntactic sugar para um `match` que retorna
cedo no caso `Err`. Ambos os estilos são válidos; `?` é mais
legível para pipelines lineares.

### Resumo dos conceitos

| Linguagem | Tipo monádico            | Erro             | Estilo principal         |
|-----------|--------------------------|------------------|--------------------------|
| Java      | `Optional<T>`            | sem informação   | `map().orElse()`         |
| Rust      | `Result<T, E>`           | com informação   | `?` ou `and_then()`      |
| Python    | `result.Result[T, E]`    | com informação   | `and_then()` ou `match`  |

O que todas têm em comum: em vez de verificar `null` ou capturar
exceções, você **compõe** o valor dentro do invólucro monádico,
decidindo o que fazer no caso normal (`Ok` / `Some`) e no caso
de falha (`Err` / `None` / `Error`) de forma explícita e segura.
