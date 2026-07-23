from undertst import mrange

def test_1_arg():
    mrange10 = mrange(10)
    assert list(mrange10) == [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]

def test_2_args():
    mrange10 = mrange(10, 15)
    assert list(mrange10) == [10, 11, 12, 13, 14]

def test_0_args():
    from itertools import islice
    assert list(islice(mrange(), 50)) == list(range(50))
    assert list(islice(mrange(), 500)) == list(range(500))
    assert list(islice(mrange(), 5000)) == list(range(5000))
