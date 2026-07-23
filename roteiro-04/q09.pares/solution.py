def naturais():
    n = 0
    while True:
        yield n
        n += 1

def pares():
    for n in naturais():
        if n % 2 == 0:
            yield n
