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


def processa(linha: str) -> Result[str, str]:
    return (
        parse_float(linha)
        .and_then(calcula_raiz)
        .and_then(calcula_inverso)
        .and_then(dobro)
        .map(lambda n: f"{n:.3f}")
    )


def processa_floats(linhas: list[str]) -> list[str]:
    return [r.unwrap() for r in map(processa, linhas) if r.is_ok()]


assert processa("16") == Ok("0.500")
assert processa("-4") == Err("erro na raiz")
assert processa("0") == Err("divisão por zero")
assert processa("abc") == Err("erro de parsing")

assert processa_floats(["16", "-4", "0", "abc", "4"]) == ["0.500", "1.000"]
