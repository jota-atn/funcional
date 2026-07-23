import math

def divisores(n):
    if n <= 0: return []
    return [x for x in range(1, n + 1) if n % x == 0]

def eh_primo(n):
    if n < 2: 
        return False
    if n == 2: 
        return True
    if n % 2 == 0: 
        return False
    
    limite = int(math.sqrt(n))
    
    return not any(n % d == 0 for d in range(3, limite + 1, 2))
