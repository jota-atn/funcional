import math
from result import Ok, Err, Result


def parse_float(linha: str) -> Result[float, str]:
    try:
        return Ok(float(linha))
    except ValueError:
        return Err("erro de parsing")


def calcula_arco_seno(x: float) -> Result[float, str]:
    if x < -1 or x > 1:
        return Err("arco inválido")
    return Ok(math.asin(x))


def calcula_raiz_cubica(x: float) -> Result[float, str]:
    return Ok(math.copysign(abs(x) ** (1 / 3), x))


def quadrado(n: float) -> Result[float, str]:
    return Ok(round(n ** 2, 3))


def processa(linha: str) -> Result[float, str]:
    return (
        parse_float(linha)
        .and_then(calcula_arco_seno)
        .and_then(calcula_raiz_cubica)
        .and_then(quadrado)
    )


assert processa("0") == Ok(0.0)
assert processa("1") == Ok(1.351)
assert processa("2") == Err("arco inválido")
assert processa("-2") == Err("arco inválido")
assert processa("abc") == Err("erro de parsing")
