import generators


def test_count():
    lst = [1, 2, 3, 1, 2, 1]
    assert list(generators.count(lst)) == [(1, 3), (2, 2), (3, 1)]
    assert list(generators.count(lst, 3)) == [(3, 1)]


def test_reversed():
    it = iter(range(5))
    it1 = generators.reversed(it)
    next(it)
    assert list(it1) == [4, 3, 2, 1]
