import generators
import inspect


def test_count():
    lst = [1, 2, 3, 1, 2, 1]
    assert list(generators.count(lst)) == [(1, 3), (2, 2), (3, 1)]
    assert list(generators.count(lst, 3)) == [(3, 1)]


def test_reversed():
    it = iter(range(5))
    it1 = generators.reversed(it)
    next(it)
    assert list(it1) == [4, 3, 2, 1]


def test_accumulate():
    it = generators.accumulate(range(1, 5))
    assert list(it) == [1, 3, 6, 10]


def test_accumulate_with_args():
    it = generators.accumulate(range(1, 5), lambda x, y: x * y)
    assert list(it) == [1, 2, 6, 24]


def test_accumulate_with_inital_value():
    it = generators.accumulate(range(1, 5), initial=-10)
    assert list(it) == [-10, -9, -7, -4, 0]


def test_chain():
    it = generators.chain([1, 2], [3], [4, 5])
    assert list(it) == [1, 2, 3, 4, 5]


def test_chain_from_iterable():
    it = generators.chain([[1, 2], [3], [4, 5]])
    assert list(it) == [1, 2, 3, 4, 5]


def test_combinations():
    it = generators.combinations([1, 2, 3])
    assert list(it) == [(1, 2, 3)]


def test_combinations_with_args():
    it = generators.combinations(range(3), 2)
    assert list(it) == [(0, 1), (0, 2), (1, 2)]


def test_combinations_with_repetition():
    it = generators.combinations_with_repetition(range(3))
    assert list(it) == [
        (0, 0, 0),
        (0, 0, 1),
        (0, 0, 2),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 2),
        (1, 1, 1),
        (1, 1, 2),
        (1, 2, 2),
        (2, 2, 2),
    ]


def test_combinations_with_repetition_with_args():
    it = generators.combinations_with_repetition(range(3), 2)
    assert list(it) == [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)]


def test_cycle():
    it = generators.cycle(range(2))
    assert (next(it), next(it), next(it), next(it)) == (0, 1, 0, 1)


def test_skip_while():
    it = generators.skip_while(range(4), lambda x: x < 1)
    assert list(it) == [1, 2, 3]


def test_skip():
    it = generators.skip(range(4), 2)
    assert list(it) == [2, 3]


def test_skip_if():
    it = generators.skip(range(4), lambda x: x % 2 == 0)
    assert list(it) == [1, 3]


def test_skip_by_mask():
    it = generators.skip(range(4), [0, 1, 0, 1])
    assert list(it) == [0, 2]


def test_group_by():
    it = generators.group_by(range(6), lambda x: int(x == 1))
    assert list(it) == [(0, (0,)), (1, (1,)), (0, (2, 3, 4, 5))]


def test_permutations():
    it = generators.permutations(range(3))
    assert list(it) == [
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    ]


def test_permutations_with_args():
    it = generators.permutations(range(3), 2)
    assert list(it) == [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]


def test_permutations_with_repetition():
    it = generators.permutations_with_repetition(range(3))
    assert list(it) == [
        (0, 0, 0),
        (0, 0, 1),
        (0, 0, 2),
        (0, 1, 0),
        (0, 1, 1),
        (0, 1, 2),
        (0, 2, 0),
        (0, 2, 1),
        (0, 2, 2),
        (1, 0, 0),
        (1, 0, 1),
        (1, 0, 2),
        (1, 1, 0),
        (1, 1, 1),
        (1, 1, 2),
        (1, 2, 0),
        (1, 2, 1),
        (1, 2, 2),
        (2, 0, 0),
        (2, 0, 1),
        (2, 0, 2),
        (2, 1, 0),
        (2, 1, 1),
        (2, 1, 2),
        (2, 2, 0),
        (2, 2, 1),
        (2, 2, 2),
    ]


def test_permutations_with_repetition_with_args():
    it = generators.permutations_with_repetition(range(3), 2)
    assert list(it) == [
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 1),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]


def test_product():
    it = generators.product(range(3), range(2))
    assert list(it) == [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


def test_take_while():
    it = generators.take_while(range(4), lambda x: x < 2)
    assert list(it) == [0, 1]


def test_take():
    it = generators.take(range(1, 4), 2)
    assert list(it) == [1, 2]


def test_take_if():
    it = generators.take(range(1, 4), lambda x: x % 2 == 1)
    assert list(it) == [1, 3]


def test_take_by_mask():
    it = generators.take(range(1, 4), [1, 0, 1])
    assert list(it) == [1, 3]


def test_reversed():
    it = generators.reversed(range(3))
    assert list(it) == [2, 1, 0]


def test_sorted():
    it = generators.sorted([5, 789345, 32])
    assert list(it) == [5, 32, 789345]


def test_split():
    it1, it2 = generators.split(range(5), 2)
    assert list(it2) == [2, 3, 4]
    assert list(it1) == [0, 1]


def test_insert():
    it = generators.insert(range(3), 1, 3)
    assert list(it) == [0, 3, 1, 2]


def test_index():
    it = generators.index([1, 2, 3, 4, 5, 4, 3], 3)
    assert list(it) == [2, 6]


def test_zip():
    it = generators.zip([1, 2, 3], ["odd", "even"])
    assert list(it) == [(1, "odd"), (2, "even")]


def test_zip_from_iterable():
    it = generators.zip([[1, 2, 3], ["odd", "even"]])
    assert list(it) == [(1, "odd"), (2, "even")]


def test_zip_longest():
    it = generators.zip([1, None], ["odd", "even"])
    assert list(it) == [(1, "odd"), (None, "even")]


def test_zip_longest_from_iterable():
    it = generators.zip([[1, None], ["odd", "even"]])
    assert list(it) == [(1, "odd"), (None, "even")]


def test_slice():
    y = list(generators.slice([1, 2, 3], 2))
    correct = [1, 2]
    assert y == correct
    y = list(generators.slice([1, 2, 3], 1, 3))
    correct = [2, 3]
    assert y == correct
    y = list(generators.slice([1, 2, 3], 0, 10, 2))
    correct = [1, 3]
    assert y == correct


def test_coverage_with_tests():
    tests = {name for name, f in globals().items() if name.startswith("test_")}
    covered_by_tests = {name.removeprefix("test_") for name in tests}
    for function_name, f in generators.__dict__.items():
        if not callable(f):
            continue
        if next(iter(inspect.signature(f).parameters.keys())) != "iterable":
            continue
        assert function_name in covered_by_tests
