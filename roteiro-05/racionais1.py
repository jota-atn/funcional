# Racional
# - racional(int, int)        => Racional
# - soma(Racional, Racional)  => Racional
# - mult(Racional, Racional)  => Racional

def toString(p):
    return f"{numer(p)}/{denom(p)}"

def racional(p, q):
    assert q != 0, "denominador de racional não pode ser zero"
    return (p, q)

def mult(p, q):
    num = numer(p) * numer(q)
    den = denom(p) * denom(q)
    produto = racional(num, den)
    return produto

def numer(p):
    return p[0]

def denom(p):
    return p[1]

# Contrato (parcial; baseado em testes)
r1 = racional(1, 2)         # 1/2
r2 = racional(1, 3)         # 1/3
#r3 = soma(r1, r2)           # 5/6
r4 = mult(r1, r2)           # 1/6
denom(r1)             # 2
numer(r2)               # 1

print(toString(r1))
print(toString(r2))
print(toString(r4))

assert numer(r1) / denom(r1) == 1 / 2

