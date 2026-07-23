class Racional:
    def __init__(self, p, q):
        assert q != 0, "denominador de racional não pode ser zero"
        self.numer = p
        self.denom = q

    def __str__(self):
        return f"{self.numer}/{self.denom}"

    def mult(p, q):
        num = p.numer * q.numer
        den = p.denom * q.denom
        produto = Racional(num, den)
        return produto


# Contrato (parcial; baseado em testes)
r1 = Racional(1, 2)         # 1/2
assert r1.numer == 1
assert r1.denom == 2
assert r1.numer / r1.denom == 1 / 2

r2 = Racional(1, 3)         # 1/3
r3 = r1.mult(r2)           # 5/6
assert r3.numer == 1
assert r3.denom == 6
