from result import Ok, Err, Result


def parse_float(linha: str) -> Result[float, str]:
    try:
        return Ok(float(linha))
    except ValueError:
        return Err("erro de parsing")


def calcula_raiz(x: float) -> Result[float, str]:
    if x < 0:
        return Err("erro na raiz")
    return Ok(x ** 0.5)


def calcula_inverso(x: float) -> Result[float, str]:
    if x == 0:
        return Err("divisão por zero")
    return Ok(1 / x)


def dobro(n: float) -> Result[float, str]:
    return Ok(n * 2)


def processa(linha: str) -> Result[float, str]:
    return (
        parse_float(linha)
        .and_then(calcula_raiz)
        .and_then(calcula_inverso)
        .and_then(dobro)
    )


assert processa("16") == Ok(0.5)
assert processa("-4") == Err("erro na raiz")
assert processa("0") == Err("divisão por zero")
assert processa("abc") == Err("erro de parsing")
