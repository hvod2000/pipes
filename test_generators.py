import pytest
import generators


generators_tests = [
    (generators.count, [[1, 2, 3, 1, 2, 1]], [(1, 3), (2, 2), (3, 1)]),
    (generators.count, [[1, 2, 3, 1, 2, 1], 3], [(3, 1)]),
    (generators.reversed, [range(5)], [4, 3, 2, 1, 0]),
    (generators.accumulate, [range(1, 5)], [1, 3, 6, 10]),
    (generators.accumulate, [range(1, 5), lambda x, y: x * y], [1, 2, 6, 24]),
    (generators.accumulate, [range(2), lambda x, y: x + y, -1], [-1, -1, 0]),
    (generators.chain, [[1, 2], [3], [4, 5]], [1, 2, 3, 4, 5]),
    (generators.chain, [[[1, 2], [3], [4, 5]]], [1, 2, 3, 4, 5]),
    (generators.combinations, [[1, 2, 3]], [(1, 2, 3)]),
    (generators.combinations, [range(3), 2], [(0, 1), (0, 2), (1, 2)]),
    (generators.combinations_with_repetition, [(0, 1)], ((0, 0), (0, 1))),
    (
        generators.combinations_with_repetition,
        [range(3), 2],
        [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2, 2)],
    ),
    (generators.cycle, [[1, 2, 3]], (1, 2, 3, 1, 2, 3, 1, 2, 3)),
    (generators.skip_while, [range(4), lambda x: x < 1], [1, 2, 3]),
    (generators.skip, [range(4), 2], [2, 3]),
    (generators.skip, [range(4), lambda x: x % 2 == 0], [1, 3]),
    (generators.skip, [range(4), [0, 1, 0, 1]], [0, 2]),
    (generators.group_by, [range(6), lambda x: int(x == 3)], ((0, (0, 1, 2)),)),
    (generators.permutations, [range(3)], ((0, 1, 2), (0, 2, 1), (1, 0, 2))),
    (generators.permutations, [range(3), 2], ((0, 1), (0, 2), (1, 0), (1, 2))),
    (
        generators.permutations_with_repetition,
        [range(3)],
        ((0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2),),
    ),
    (
        generators.permutations_with_repetition,
        [range(3), 2],
        ((0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0),),
    ),
    (
        generators.product,
        [range(3), range(2)],
        [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)],
    ),
    (generators.take_while, [range(4), lambda x: x < 2], [0, 1]),
    (generators.take, [range(1, 4), 2], [1, 2]),
    (generators.take, [range(1, 4), lambda x: x % 2 == 1], [1, 3]),
    (generators.take, [range(1, 4), [1, 0, 1]], [1, 3]),
    (generators.reversed, [range(3)], [2, 1, 0]),
    (generators.sorted, [[]], []),
    (generators.sorted, [[3, 2, 1]], [1, 2, 3]),
    (generators.sorted, [[5, 789345, 32]], [5, 32, 789345]),
    (generators.split, [[1, 2, 3, 4, 5], 0], [(), (1, 2, 3, 4, 5)]),
    (generators.split, [[1, 2, 3, 4, 5], 5], [(1, 2, 3, 4, 5), ()]),
    (generators.split, [[1, 2, 3, 4, 5], 2], [(1, 2), (3, 4, 5)]),
    (generators.insert, [[1, 2, 3], 1, 9], [1, 9, 2, 3]),
    (generators.insert, [["start"], 1, "end"], ["start", "end"]),
    (generators.insert, [[], 0, 9], [9]),
    (generators.index, [[1, 2, 3], 4], []),
    (generators.index, [[1, 2, 3, 4], 4], [3]),
    (generators.index, [[4, 2, 3, 4], 4], [0, 3]),
    (generators.zip, [[1, 2], [3, 4, 5]], [(1, 3), (2, 4)]),
    (generators.zip, [[[1, 2], [3, 4, 5]]], [(1, 3), (2, 4)]),
    (generators.zip_longest, [[1], [2, 3]], [(1, 2), (None, 3)]),
    (generators.zip_longest, [[[1], [2, 3]]], [(1, 2), (None, 3)]),
    (generators.zip_longest, [[1, 2], [3, 4, 5]], [(1, 3), (2, 4), (None, 5)],),
    (generators.slice, [[1, 2, 3], 2], [1, 2]),
    (generators.slice, [[1, 2, 3], 1, 3], [2, 3]),
    (generators.slice, [[1, 2, 3], 0, 10, 2], [1, 3]),
]


@pytest.mark.parametrize("f, args, expected_result", generators_tests)
def test_generators(f, args, expected_result):
    result = (x if isinstance(x, (int, str)) else tuple(x) for x in f(*args))
    if not isinstance(expected_result, list):
        for y, expected_y in zip(result, expected_result):
            assert y == expected_y
        return
    assert list(result) == expected_result


def test_coverage_with_tests():
    covered_by_tests = {f.__name__ for f, _, _ in generators_tests}
    for function_name, f in generators.__dict__.items():
        if callable(f) and "iterable" in f.__code__.co_varnames:
            assert function_name in covered_by_tests
