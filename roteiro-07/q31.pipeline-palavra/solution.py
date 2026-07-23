from result import Ok, Err, Result


def parse_palavra(linha: str) -> Result[str, str]:
    if linha == "":
        return Err("palavra vazia")
    if not linha.isalpha():
        return Err("caractere inválido")
    return Ok(linha)


def verifica_vogais(s: str) -> Result[str, str]:
    if not any(c in "aeiouAEIOU" for c in s):
        return Err("sem vogais")
    return Ok(s)


def gritar(s: str) -> Result[str, str]:
    return Ok(s.upper())


def inverter(s: str) -> Result[str, str]:
    return Ok(s[::-1])


def processa(linha: str) -> Result[str, str]:
    return (
        parse_palavra(linha)
        .and_then(verifica_vogais)
        .and_then(gritar)
        .and_then(inverter)
    )


assert processa("ola") == Ok("ALO")
assert processa("") == Err("palavra vazia")
assert processa("pygmy") == Err("sem vogais")
assert processa("123") == Err("caractere inválido")
