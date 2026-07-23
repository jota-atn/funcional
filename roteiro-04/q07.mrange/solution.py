from itertools import count

def mrange(*args):
    n = len(args)
    
    if n == 0:
        return count(0)
    
    return iter(range(*args))
