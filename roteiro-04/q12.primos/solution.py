import math

def naturais():
    n = 0
    while True:
        yield n
        n += 1

def eh_primo(n):
    if n < 2: 
        return False
    if n == 2: 
        return True
    if n % 2 == 0: 
        return False
    
    limite = int(math.sqrt(n))
    return not any(n % d == 0 for d in range(3, limite + 1, 2))

def primos():
    return (n for n in naturais() if eh_primo(n))
