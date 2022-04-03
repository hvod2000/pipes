import unittest
from myiters import Iter

lst = [1, 2, 3]


class ItertoolsFunctionalityTestCase(unittest.TestCase):
    def test_apply(self):
        y = Iter(lst).apply(lambda x, y, z: list(x) + [4, 5], 1, 0) / list
        self.assertEqual(y, [1, 2, 3, 4, 5])

    def test_copy(self):
        it1 = Iter([1, 2, 3])
        it2 = it1.copy()
        y = (list(it1), list(it2))
        correct = ([1, 2, 3], [1, 2, 3])
        self.assertEqual(y, correct)

    def test_user_defined_methods(self):
        log = []

        def custom_function(iterable, lst):
            log.extend(iterable)
            yield from lst

        self.assertEqual(log, [])
        y = Iter(lst).custom_function(["TA"]) / next
        self.assertEqual(log, [1, 2, 3])
        correct = "TA"
        self.assertEqual(y, correct)

    def test_iter_metamethod(self):
        it = Iter(lst)
        y = (next(it), next(it), next(it))
        correct = (1, 2, 3)
        self.assertEqual(y, correct)

    def test_accumulate(self):
        self.assertEqual(Iter(lst).accumulate() / list, [1, 3, 6])

    def test_accumulate_with_args(self):
        y = Iter(lst).accumulate(lambda x, y: x * y) / list
        correct = [1, 2, 6]
        self.assertEqual(y, correct)

    def test_chain(self):
        y = Iter([[1, 2], [3], [4, 5]]).chain() / list
        correct = [1, 2, 3, 4, 5]
        self.assertEqual(y, correct)

    def test_chain_with_args(self):
        y = Iter(lst).chain(lst) / list
        correct = [1, 2, 3, 1, 2, 3]
        self.assertEqual(y, correct)

    def test_combinations(self):
        y = Iter(lst).combinations() / list
        correct = [(1, 2, 3)]
        self.assertEqual(y, correct)

    def test_combinations_with_args(self):
        y = Iter(lst).combinations(2) / list
        correct = [(1, 2), (1, 3), (2, 3)]
        self.assertEqual(y, correct)

    def test_combinations_with_repetition(self):
        y = Iter(lst).combinations_with_repetition() / list
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
        self.assertEqual(y, correct)

    def test_combinations_with_repetition_with_args(self):
        y = Iter(lst).combinations_with_repetition(2) / list
        correct = [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]
        self.assertEqual(y, correct)

    def test_compress(self):
        y = Iter(lst).compress([0, 1]) / list
        correct = [2]
        self.assertEqual(y, correct)
        y = Iter(lst).compress([1, 0, 1, 1]) / list
        correct = [1, 3]
        self.assertEqual(y, correct)

    def test_cycle(self):
        y = Iter(lst).cycle().slice(5) / list
        correct = [1, 2, 3, 1, 2]
        self.assertEqual(y, correct)

    def test_skip_while(self):
        y = Iter(lst).skip_while(lambda x: x < 2) / list
        correct = [2, 3]
        self.assertEqual(y, correct)

    def test_skip_if(self):
        y = Iter(lst).skip_if(lambda x: x == 2) / list
        correct = [1, 3]
        self.assertEqual(y, correct)

    def test_group_by(self):
        y = Iter(lst).group_by(lambda x: int(x == 1)) / list
        correct = [(1, (1,)), (0, (2, 3))]
        self.assertEqual(y, correct)

    def test_slice(self):
        y = Iter(lst).slice(2) / list
        correct = [1, 2]
        self.assertEqual(y, correct)
        y = Iter(lst).slice(1, 3) / list
        correct = [2, 3]
        self.assertEqual(y, correct)
        y = Iter(lst).slice(0, 10, 2) / list
        correct = [1, 3]
        self.assertEqual(y, correct)

    def test_permutations(self):
        y = Iter(lst).permutations() / list
        correct = [
            (1, 2, 3),
            (1, 3, 2),
            (2, 1, 3),
            (2, 3, 1),
            (3, 1, 2),
            (3, 2, 1),
        ]
        self.assertEqual(y, correct)

    def test_permutations_with_args(self):
        y = Iter(lst).permutations(2) / list
        correct = [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
        self.assertEqual(y, correct)

    def test_permutations_with_repetition(self):
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
        self.assertEqual(y, correct)

    def test_permutations_with_repetition_with_args(self):
        y = Iter(lst).permutations_with_repetition(2) / list
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
        self.assertEqual(y, correct)

    def test_product(self):
        y = Iter(lst).product(lst) / list
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
        self.assertEqual(y, correct)

    def test_take_while(self):
        y = Iter(lst).take_while(lambda x: x < 3) / list
        correct = [1, 2]
        self.assertEqual(y, correct)

    def test_duplicate(self):
        it1 = Iter(lst)
        it2, it3 = it1.duplicate()
        y = (next(it1), next(it2), next(it3))
        correct = (1, 2, 2)
        self.assertEqual(y, correct)

    def test_zip_longest(self):
        it1 = Iter(range(2))
        it2 = Iter(range(3))
        y = it1.zip_longest(it2) / list
        correct = [(0, 0), (1, 1), (None, 2)]
        self.assertEqual(y, correct)

    def test_take_if(self):
        y = Iter(lst).take_if(lambda x: x % 2 == 1) / list
        correct = [1, 3]
        self.assertEqual(y, correct)

    def test_filter(self):
        y = Iter(lst).filter(lambda x: x % 2 == 1) / list
        correct = [1, 3]
        self.assertEqual(y, correct)

    def test_map(self):
        y = Iter(lst).map(lambda x: x ** 2) / list
        correct = [1, 4, 9]
        self.assertEqual(y, correct)

    def test_starmap(self):
        y = Iter(range(3)).product(repeat=2).starmap(lambda x, y: x * y) / list
        correct = [0, 0, 0, 0, 1, 2, 0, 2, 4]
        self.assertEqual(y, correct)

    def test_reversed(self):
        y = Iter(lst).reversed() / list
        correct = [3, 2, 1]
        self.assertEqual(y, correct)

    def test_sorted(self):
        y = Iter(lst).reversed().sorted() / list
        correct = lst
        self.assertEqual(y, correct)

    def test_zip(self):
        it1 = Iter(range(2))
        it2 = Iter(range(3))
        y = it1.zip(it2) / list
        correct = [(0, 0), (1, 1)]
        self.assertEqual(y, correct)

    def test_split(self):
        it1, it2 = Iter(range(10)).split(5)
        y = (next(it1), list(it2))
        correct = (0, [5, 6, 7, 8, 9])
        self.assertEqual(y, correct)

    def test_insert(self):
        y = Iter(lst).insert(1, 123) / list
        correct = [1, 123, 2, 3]
        self.assertEqual(y, correct)

    def test_index(self):
        y = Iter([1, 2, 3, 4, 5, 3]).index(3) / list
        correct = [2, 5]
        self.assertEqual(y, correct)


if __name__ == "__main__":
    unittest.main()
