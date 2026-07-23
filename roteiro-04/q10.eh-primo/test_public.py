from undertst import eh_primo, divisores

def test_1_nao_eh():
    assert not eh_primo(1)

def test_nao_sao():
    NAO_PRIMOS = [0, 1, 4, 6, 8, 9, 10, 12, 70, 187, 371, 763]
    assert not any(eh_primo(n) for n in NAO_PRIMOS)

def test_sao():
    PRIMOS = [2, 3, 5, 7, 11, 13, 127, 251, 419, 557, 929]
    assert all(eh_primo(n) for n in PRIMOS)

def test_divisores_4():
    assert list(divisores(10)) == [1, 2, 5, 10]
