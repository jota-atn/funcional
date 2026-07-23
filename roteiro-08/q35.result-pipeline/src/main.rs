// q35.result-pipeline — Tratamento monádico de erros com Result em Rust
//
// Instruções:
//   1. Implemente as funções abaixo seguindo as assinaturas fornecidas.
//   2. Use o operador ? para propagar erros de forma monádica.
//   3. Execute `cargo test` para verificar.
//
// Comportamento esperado:
//   find_user(1)    -> Ok(&User("Alice", Some("alice@example.com")))
//   find_user(99)   -> Err("Usuário 99 não encontrado")
//   get_email(Alice) -> Ok("alice@example.com")
//   get_email(Bob)   -> Err("Bob não possui email")
//   notify_user(1)   -> Ok("Enviando email para Alice em <alice@example.com>")
//   notify_user(2)   -> Err("Bob não possui email")
//   notify_multiple(&[1,2,3]) -> ["Enviando email para Alice em <alice@example.com>",
//                                 "Enviando email para Carol em <carol@test.com>"]

#[derive(Debug, PartialEq)]
struct User {
    name: &'static str,
    email: Option<&'static str>,
}

static USERS: &[(u32, User)] = &[
    (1, User { name: "Alice", email: Some("alice@example.com") }),
    (2, User { name: "Bob",   email: None }),
    (3, User { name: "Carol", email: Some("carol@test.com") }),
];

/// Busca um usuário pelo ID.
/// Retorna Err se o ID não for encontrado.
fn find_user(id: u32) -> Result<&'static User, String> {
    USERS
        .iter()
        .find(|(user_id, _)| *user_id == id)
        .map(|(_, user)| user)
        .ok_or_else(|| format!("Usuário {id} não encontrado"))
}

/// Extrai o email de um usuário.
/// Retorna Err se o usuário não tiver email cadastrado.
fn get_email(user: &User) -> Result<&'static str, String> {
    user.email
        .ok_or_else(|| format!("{} não possui email", user.name))
}

/// Compõe find_user + get_email com o operador ?.
/// Retorna uma mensagem formatada: "Enviando email para {nome} em <{email}>"
fn notify_user(id: u32) -> Result<String, String> {
    let user = find_user(id)?;
    let email = get_email(user)?;
    Ok(format!("Enviando email para {} em <{}>", user.name, email))
}

/// Processa uma lista de IDs e coleta apenas as notificações bem-sucedidas.
/// Use iteradores — sem laços explícitos.
fn notify_multiple(ids: &[u32]) -> Vec<String> {
    ids.iter()
        .map(|&id| notify_user(id))
        .filter_map(Result::ok)
        .collect()
}

// ───── testes ─────

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn find_existing_user() {
        let user = find_user(1).unwrap();
        assert_eq!(user.name, "Alice");
    }

    #[test]
    fn find_missing_user() {
        assert_eq!(find_user(99), Err("Usuário 99 não encontrado".to_string()));
    }

    #[test]
    fn get_valid_email() {
        let user = find_user(1).unwrap();
        assert_eq!(get_email(user), Ok("alice@example.com"));
    }

    #[test]
    fn get_missing_email() {
        let user = find_user(2).unwrap();
        assert_eq!(get_email(user), Err("Bob não possui email".to_string()));
    }

    #[test]
    fn notify_valid_user() {
        assert_eq!(
            notify_user(1),
            Ok("Enviando email para Alice em <alice@example.com>".to_string())
        );
    }

    #[test]
    fn notify_user_without_email() {
        assert!(notify_user(2).is_err());
    }

    #[test]
    fn notify_nonexistent_user() {
        assert!(notify_user(99).is_err());
    }

    #[test]
    fn notify_multiple_mixed() {
        let result = notify_multiple(&[1, 2, 3, 99]);
        assert_eq!(result, vec![
            "Enviando email para Alice em <alice@example.com>",
            "Enviando email para Carol em <carol@test.com>",
        ]);
    }

    #[test]
    fn notify_multiple_empty() {
        assert!(notify_multiple(&[]).is_empty());
    }

    #[test]
    fn notify_multiple_all_invalid() {
        assert!(notify_multiple(&[2, 99]).is_empty());
    }
}
