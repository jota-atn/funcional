from undertst import primos

def test_1():
    from itertools import islice
    assert list(islice(primos(), 4)) == [2, 3, 5, 7]
