from myiters import Iter
import pytest


def test_apply():
    y = Iter([1, 2, 3]).apply(lambda x, y, z: list(x) + [4, 5], 1, 0) / list
    assert y == ([1, 2, 3, 4, 5])


def test_copy():
    it1 = Iter([1, 2, 3])
    it2 = it1.copy()
    y = (list(it1), list(it2))
    correct = ([1, 2, 3], [1, 2, 3])
    assert y == correct


def test_user_defined_methods():
    log = []

    def custom_function(iterable, lst):
        log.extend(iterable)
        yield from lst

    assert log == []
    y = Iter([1, 2, 3]).custom_function(["TA"]) / next
    assert log == [1, 2, 3]
    correct = "TA"
    assert y == correct


def test_iter_metamethod():
    it = Iter([1, 2, 3])
    y = (next(it), next(it), next(it))
    correct = (1, 2, 3)
    assert y == correct


def test_accumulate():
    y = Iter([1, 2, 3]).accumulate() / list
    correct = [1, 3, 6]
    assert y == correct


def test_accumulate_with_args():
    y = Iter([1, 2, 3]).accumulate(lambda x, y: x * y) / list
    correct = [1, 2, 6]
    assert y == correct


def test_chain():
    y = Iter([[1, 2], [3], [4, 5]]).chain() / list
    correct = [1, 2, 3, 4, 5]
    assert y == correct


def test_chain_with_args():
    y = Iter([1, 2, 3]).chain([1, 2, 3]) / list
    correct = [1, 2, 3, 1, 2, 3]
    assert y == correct


def test_combinations():
    y = Iter([1, 2, 3]).combinations() / list
    correct = [(1, 2, 3)]
    assert y == correct


def test_combinations_with_args():
    y = Iter([1, 2, 3]).combinations(2) / list
    correct = [(1, 2), (1, 3), (2, 3)]
    assert y == correct


def test_combinations_with_repetition():
    y = Iter([1, 2, 3]).combinations_with_repetition() / list
    correct = [
        (1, 1, 1),
        (1, 1, 2),
        (1, 1, 3),
        (1, 2, 2),
        (1, 2, 3),
        (1, 3, 3),
        (2, 2, 2),
        (2, 2, 3),
        (2, 3, 3),
        (3, 3, 3),
    ]
    assert y == correct


def test_combinations_with_repetition_with_args():
    y = Iter([1, 2, 3]).combinations_with_repetition(2) / list
    correct = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
    assert y == correct


def test_cycle():
    y = Iter([1, 2, 3]).cycle().slice(5) / list
    correct = [1, 2, 3, 1, 2]
    assert y == correct


def test_skip_while():
    y = Iter([1, 2, 3]).skip_while(lambda x: x < 2) / list
    correct = [2, 3]
    assert y == correct


def test_skip():
    it = Iter(range(4)).skip(2)
    assert list(it) == [2, 3]


def test_skip_if():
    y = Iter([1, 2, 3]).skip(lambda x: x == 2) / list
    correct = [1, 3]
    assert y == correct


def test_skip_by_mask():
    it = Iter(range(4)).skip([0, 1, 0, 1])
    assert list(it) == [0, 2]


def test_group_by():
    y = Iter([1, 2, 3]).group_by(lambda x: int(x == 1)) / list
    correct = [(1, (1,)), (0, (2, 3))]
    assert y == correct


def test_slice():
    y = Iter([1, 2, 3]).slice(2) / list
    correct = [1, 2]
    assert y == correct
    y = Iter([1, 2, 3]).slice(1, 3) / list
    correct = [2, 3]
    assert y == correct
    y = Iter([1, 2, 3]).slice(0, 10, 2) / list
    correct = [1, 3]
    assert y == correct


def test_permutations():
    y = Iter([1, 2, 3]).permutations() / list
    correct = [
        (1, 2, 3),
        (1, 3, 2),
        (2, 1, 3),
        (2, 3, 1),
        (3, 1, 2),
        (3, 2, 1),
    ]
    assert y == correct


def test_permutations_with_args():
    y = Iter([1, 2, 3]).permutations(2) / list
    correct = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
    assert y == correct


def test_permutations_with_repetition():
    y = Iter(range(3)).permutations_with_repetition() / list
    correct = [
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
    assert y == correct


def test_permutations_with_repetition_with_args():
    y = Iter([1, 2, 3]).permutations_with_repetition(2) / list
    correct = [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    ]
    assert y == correct


def test_product():
    y = Iter([1, 2, 3]).product([1, 2, 3]) / list
    correct = [
        (1, 1),
        (1, 2),
        (1, 3),
        (2, 1),
        (2, 2),
        (2, 3),
        (3, 1),
        (3, 2),
        (3, 3),
    ]
    assert y == correct


def test_take_while():
    y = Iter([1, 2, 3]).take_while(lambda x: x < 3) / list
    correct = [1, 2]
    assert y == correct


def test_copy_into_many():
    it1 = Iter([1, 2, 3])
    it2, it3 = it1.copy(2)
    y = (next(it1), next(it2), next(it3))
    correct = (1, 2, 2)
    assert y == correct


def test_zip_longest():
    it1 = Iter(range(2))
    it2 = Iter(range(3))
    y = it1.zip_longest(it2) / list
    correct = [(0, 0), (1, 1), (None, 2)]
    assert y == correct


def test_take():
    it = Iter(range(1, 4)).take(2)
    assert list(it) == [1, 2]


def test_take_if():
    y = Iter([1, 2, 3]).take(lambda x: x % 2 == 1) / list
    correct = [1, 3]
    assert y == correct


def test_take_by_mask():
    it = Iter(range(1, 4)).take([1, 0, 1])
    assert list(it) == [1, 3]


def test_map():
    y = Iter([1, 2, 3]).map(lambda x: x ** 2) / list
    correct = [1, 4, 9]
    assert y == correct


def test_starmap():
    y = Iter(range(3)).product(repeat=2).starmap(lambda x, y: x * y) / list
    correct = [0, 0, 0, 0, 1, 2, 0, 2, 4]
    assert y == correct


def test_reversed():
    y = Iter([1, 2, 3]).reversed() / list
    correct = [3, 2, 1]
    assert y == correct


def test_sorted():
    y = Iter([1, 2, 3]).reversed().sorted() / list
    correct = [1, 2, 3]
    assert y == correct


def test_zip():
    it1 = Iter(range(2))
    it2 = Iter(range(3))
    y = it1.zip(it2) / list
    correct = [(0, 0), (1, 1)]
    assert y == correct


def test_split():
    it1, it2 = Iter(range(10)).split(5)
    y = (next(it1), list(it2))
    correct = (0, [5, 6, 7, 8, 9])
    assert y == correct


def test_insert():
    y = Iter([1, 2, 3]).insert(1, 123) / list
    correct = [1, 123, 2, 3]
    assert y == correct


def test_index():
    y = Iter([1, 2, 3, 4, 5, 3]).index(3) / list
    correct = [2, 5]
    assert y == correct


def test_next():
    it = Iter([1, 2, 3, 4, 5])
    assert next(it) == 1
    assert next(it) == 2
    assert next(it) == 3
    assert next(it) == 4
    assert next(it) == 5
    with pytest.raises(StopIteration):
        next(it)


def test_next_on_copy():
    original = Iter([1, 2, 3, 4, 5])
    cheap_copy = original.copy()
    assert next(original) == 1
    assert next(original) == 2
    assert next(cheap_copy) == 1
    assert next(original) == 3
    assert next(cheap_copy) == 2


def test_simple_composition():
    it0 = Iter(range(123))
    it1 = (
        it0.apply(lambda x, y, z=2: x, y=1, z=3)
        .accumulate(lambda x, y: y - 3)
        .chain(it0)
        .take([1] * 100)
        .skip_while(lambda x: x < 10)
        .skip(lambda x: x % 3 == 0)
        .group_by(lambda x: x // 10)
        .slice(5)
        .take_while(lambda x: x[0] < 4)
        .take(lambda x: x[0] > 0)
        .accumulate(lambda x, y: [0, x[1] + y[1]])
        .slice(2, 3)
        .map(lambda x: x[1])
        .map(lambda x: sum(x))
    )
    _ = it0.slice(3).now()
    assert next(it1) == 480


def test_square():
    it0 = Iter(range(2 ** 32))
    it1 = (
        it0.map(lambda x: x - 9)
        .take(lambda x: x % 2 == 1)
        .map(lambda x: (x, -x, x))
        .starmap(lambda x, y, z: sum([x, y, z]))
    )
    _ = it0.slice(0, 10, 1).now()
    for n in range(10):
        assert it1.copy().slice(n) / sum == n ** 2


@pytest.mark.parametrize(
    "method, args",
    [
        (Iter.accumulate, []),
        (Iter.chain, []),
        (Iter.combinations, [3]),
        (Iter.combinations_with_repetition, [3],),
        (Iter.take, [[0, 1] * 2]),
        (Iter.cycle, []),
        (Iter.skip_while, [lambda x: x[0] < 10]),
        (Iter.skip, [lambda x: len(x)]),
        (Iter.group_by, []),
        (Iter.slice, [321]),
        (Iter.permutations, [5]),
        (Iter.permutations_with_repetition, [5],),
        (Iter.product, [list(range(3))]),
        (Iter.take_while, [lambda x: x]),
        (Iter.zip_longest, [list(range(3))]),
        (Iter.take, [lambda x: x]),
        (Iter.map, [lambda x: x]),
        (Iter.starmap, [lambda x, y, z: (x + y, y + z, z + x)]),
        (Iter.reversed, []),
        (Iter.sorted, []),
        (Iter.zip, [list(range(4))]),
        (Iter.insert, [2, "I AM HERE"]),
        (Iter.index, [[15, 16, 17]]),
    ],
)
def test_laziness(method, args):
    lst = [list(range(i * 3, (i + 1) * 3)) for i in range(10)]
    it1 = Iter(lst)
    y0 = method(it1.copy().slice(2, None), *args).slice(10) / list
    it2 = method(it1, *args)
    _ = it1.slice(0, 2).now()
    y1 = it2.slice(10) / list
    assert y0 == y1
