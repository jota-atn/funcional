from undertst import naturais

def test_funciona():
    from itertools import islice
    assert list(islice(naturais(), 5)) == [0, 1, 2, 3, 4]
    assert list(islice(naturais(), 10)) == list(range(10))
    assert list(islice(naturais(), 100)) == list(range(100))
    assert list(islice(naturais(), 1000)) == list(range(1000))
