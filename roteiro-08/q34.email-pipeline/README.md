# Exercício: Pipeline de notificações com Optional e Stream

## Objetivo

Praticar a construção de um pipeline de processamento usando
`Stream` e `Optional`, compondo as operações de forma monádica
como código **cliente** de tipos que já usam `Optional`.

## Contexto

Este exercício aproveita o `EmailService` e o `User` do exercício
anterior (`q33.getEmail`). Suponha que temos:

- `UserRepository` — retorna `Optional<User>` ao buscar por ID
  (um usuário pode não existir)
- `EmailService.getEmail(Optional<User>)` — retorna o email em
  minúsculas ou `"email não disponível"`
- `NotificationService` — deve montar mensagens de notificação
  para uma lista de IDs de usuário

## O que fazer

Implemente o método `buildNotificationMessages` em
`NotificationService` para que ele:

1. Receba uma `List<Integer>` contendo IDs de usuário
2. Para cada ID, busque o `User` no repositório
3. Obtenha o email através do `EmailService`
4. **Filtre** os resultados inválidos (onde o email é `"email não disponível"`)
5. Transforme cada email válido em `"Enviando email para {email}"`
6. Recolha os resultados em uma `List<String>`

Faça tudo usando a API de `Stream` (**map**, **filter**,
**collect**), sem usar laços `for` ou `while`.

## Exemplos de comportamento

| Entrada         | Resultado                                                                         |
|-----------------|-----------------------------------------------------------------------------------|
| `[1, 2, 3, 99]` | `["Enviando email para alice@example.com", "Enviando email para carol@test.com"]` |
| `[]`            | `[]`                                                                              |
| `[2, 99]`       | `[]`                                                                              |

> **Nota sobre os IDs:** o repositório contém Alice (id 1, email
> válido), Bob (id 2, email `null`) e Carol (id 3, email válido).
> IDs inexistentes retornam `Optional.empty()`.

## Abordagens alternativas em outras linguagens

O `Optional` do Java usa composição funcional (`map`, `flatMap`,
`orElse`) para lidar com valores ausentes sem verificações
explícitas. Outras linguagens oferecem o mesmo conceito, mas com
sintaxe diferente:

### Rust — `Option<T>` com pattern matching

Rust tem `Option<T>` como uma **enum** nativa. O programador pode usar `match` (pattern matching) ou métodos funcionais:

```rust
fn get_email(user: Option<User>) -> String {
    match user {
        Some(u) => match u.email() {
            Some(e) => e.to_lowercase(),
            None    => String::from("email não disponível"),
        },
        None => String::from("email não disponível"),
    }
}
```

Ou, funcionalmente (equivalente ao que você fez em Java):

```rust
fn get_email(user: Option<User>) -> String {
    user.and_then(|u| u.email())
        .map(|e| e.to_lowercase())
        .unwrap_or_else(|| String::from("email não disponível"))
}
```

### Python — pacote `result`

Python não tem um tipo `Optional` nativo que force o tratamento,
mas o pacote [`result`](https://pypi.org/project/result/) (que
vocês já conhecem) oferece `Ok` / `Error` com pattern matching
via `match` (Python 3.10+):

```python
from result import Ok, Error

def get_email(user: Result[User, str]) -> str:
    match user:
        case Ok(u) if u.email:
            return u.email.lower()
        case _:
            return "email não disponível"
```

Ou, funcionalmente (encadeando `map` / `map_err` / `unwrap_or`):

```python
def get_email(user: Result[User, str]) -> str:
    return (user
            .map(lambda u: u.email)
            .map(lambda e: e.lower() if e else None)
            .unwrap_or("email não disponível"))
```

### Por que Java não usa pattern matching com `Optional`?

Em Rust, `Option` é uma **enum** (ou tipo soma / discriminated
union), então o compilador sabe exatamente quais variantes
existem (`Some` e `None`) e pode exigi-las num `match`. Em Java,
`Optional` foi criado como uma classe comum (não uma `sealed
interface` ou `enum`), então não é possível destruturá-la com
`switch` ou `instanceof` — ela só oferece a API funcional (`map`,
`filter`, `orElse`, etc.).

Cada linguagem faz uma escolha de projeto: `Optional` prioriza a
**composição funcional**; tipos soma (Rust, Python com `result`,
Scala, Haskell) priorizam o **pattern matching** combinado com a
mesma API funcional.

## Compilando e executando

Compilar:

```bash
javac User.java EmailService.java UserRepository.java NotificationService.java NotificationServiceTest.java
```

Executar os testes:

```bash
java NotificationServiceTest
```
