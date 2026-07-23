# Exercício: Optional monádico em Java

## Objetivo

Praticar o uso de `Optional<T>` em Java para lidar com valores potencialmente ausentes de forma monádica, substituindo verificações explícitas de `null`.

## Descrição

Considere a seguinte classe `User`:

```java
public class User {
    private String name;
    private String email;

    public User(String name, String email) {
        this.name = name;
        this.email = email;
    }

    public String getEmail() {
        return email;
    }
}
```

Suponha que você tenha uma classe `EmailService` com um método `getEmail(User user)` cujo objetivo é retornar o email do usuário em letras minúsculas.

### Parte 1 — Implementação com null (ponto de partida didático)

Implemente `getEmail` da forma tradicional, verificando se o parâmetro `user` é `null` e se o email dentro do usuário é `null`. Se qualquer um for `null`, retorne `"email não disponível"`.

> **Nota:** Esta versão existe apenas como etapa didática. No código real, receber `User` (que pode ser `null`) obriga o程序 a fazer verificações defensivas espalhadas por todo o código. O `Optional` resolve exatamente esse problema, como veremos a seguir.

```java
public class EmailService {
    public String getEmail(User user) {
        // sua implementação aqui
    }
}
```

### Parte 2 — Refatoração com Optional (versão definitiva)

Agora refatore o código para que `getEmail` receba um `Optional<User>` em vez de `User` diretamente. Utilize a API de `Optional` de forma **monádica** (encadeando chamadas como `map`, `flatMap`, `orElse`, etc.) **sem usar `if` explícito ou `isPresent()`/`get()`**.

> **Nota:** Esta é a versão que usaríamos em código real. O `Optional` já documenta na assinatura do método que o valor pode estar ausente, e a implementação monádica elimina a necessidade de qualquer verificação explícita de `null`.

O comportamento esperado é o mesmo:
- Se o `Optional` estiver vazio → retornar `"email não disponível"`
- Se o `User` existir mas o email for `null` → retornar `"email não disponível"`
- Caso contrário → retornar o email em letras minúsculas

```java
public class EmailService {
    public String getEmail(Optional<User> user) {
        // sua implementação aqui — estilo monádico, sem if/isPresent/get
    }
}
```

## Exemplos de comportamento

| Entrada                                               | Resultado                |
|-------------------------------------------------------|--------------------------|
| `Optional.of(new User("Alice", "Alice@Example.com"))` | `"alice@example.com"`    |
| `Optional.of(new User("Bob", null))`                  | `"email não disponível"` |
| `Optional.empty()`                                    | `"email não disponível"` |

## Compilando e executando

Execute todos os comandos **neste diretório** (onde está este README).

Compilar:

```bash
javac User.java EmailService.java EmailServiceTest.java
```

Executar os testes:

```bash
java EmailServiceTest
```

## Dica

Consulte os métodos `map`, `flatMap` e `orElse` da classe `java.util.Optional`.
