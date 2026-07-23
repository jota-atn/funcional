def divisores(n):
    return [x for x in range(1, n + 1) if n % x == 0]

def eh_primo(n):
    if n <= 1:
        return False
    
    return divisores(n) == [1, n]
