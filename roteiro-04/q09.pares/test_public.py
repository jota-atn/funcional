from undertst import pares

def test_funciona():
    from itertools import islice
    assert list(islice(pares(), 5)) == [0, 2, 4, 6, 8]
    assert list(islice(pares(), 10)) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
