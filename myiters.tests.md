# TESTS
```python
>>> from myiters import Iter
>>> lst100, lst5 = list(range(1, 101)), [1, 2, 3, 4, 5]
>>> Iter(lst5).apply(lambda x, y: list(x) + [y], "end") / list
[1, 2, 3, 4, 5, 'end']


>>> iter1 = Iter(lst5)
>>> iter2 = iter1
>>> print(next(iter1), next(iter2))
1 2

>>> iter1 = Iter(lst5)
>>> iter2 = iter1.copy()
>>> print(next(iter1), next(iter2))
1 1

>>> def my_function(items):
...     for item in items:
...         print(item)
...     yield from ()
>>> it = Iter(range(2)).my_function()
>>> _ = it.now()
0
1

>>> it1 = iter(range(1, 5))
>>> it2 = Iter(it1)
>>> print(next(it1), next(it2), next(it1), next(it2))
1 2 3 4

>>> it0 = Iter(range(4))
>>> it1 = (
...     it0.accumulate(lambda x, y: x - y)
...     .chain([5, 4])
...     .compress([0, 0, 1, 0, 1])
...     .slice(2)
...     .product([0, 1])
...     .cycle()
...     .slice(8)
... )
>>> print(next(it0), it1 / list)
0 [(-4, 0), (-4, 1), (4, 0), (4, 1), (-4, 0), (-4, 1), (4, 0), (4, 1)]


>>> it0 = Iter(range(123))
>>> it1 = (
...     it0.apply(lambda x, y, z=2: x, y=1, z=3)
...     .accumulate(lambda x, y: y - 3)
...     .chain(it0)
...     .compress([1] * 100)
...     .skip_while(lambda x: x < 10)
...     .skip_if(lambda x: x % 3 == 0)
...     .group_by(lambda x: x // 10)
...     .slice(5)
...     .take_while(lambda x: x[0] < 4)
...     .take_if(lambda x: x[0] > 0)
...     .accumulate(lambda x, y: [0, x[1] + y[1]])
...     .slice(2, 3)
...     .map(lambda x: x[1])
...     .map(lambda x: sum(x))
... )
>>> _ = it0.slice(3).now()
>>> print(it1 / next)
480


>>> it0 = Iter(range(123))
>>> it1 = (
...     it0.map(lambda x: x - 9)
...     .take_if(lambda x: x % 2 == 1)
...     .map(lambda x: (x, -x, x))
...     .starmap(lambda x, y, z: sum([x, y, z]))
...     .slice(11)
...     .reversed()
... )
>>> it2 = it1.copy()
>>> _ = it0.slice(0, 10, 1).now()
>>> print(it1 / sum, it2.sorted().slice(5) / sum)
121 25


>>> for name, method, args, *postprocessings in (
...     ("accumulate", Iter.accumulate, []),
...     ("chain", Iter.chain, []),
...     ("combinations", Iter.combinations, [3]),
...     ("combinations_with_repetition", Iter.combinations_with_repetition, [3]),
...     ("compress", Iter.compress, [[0, 1] * 2]),
...     ("cycle", Iter.cycle, []),
...     ("skip_while", Iter.skip_while, [lambda x: x[0] < 10]),
...     ("skip_if", Iter.skip_if, [lambda x: len(x)]),
...     ("group_by", Iter.group_by, []),
...     ("slice", Iter.slice, [321]),
...     ("permutations", Iter.permutations, [5]),
...     ("permutations_with_repetition", Iter.permutations_with_repetition, [5]),
...     ("product", Iter.product, [list(range(3))]),
...     ("take_while", Iter.take_while, [lambda x: x]),
...     ("zip_longest", Iter.zip_longest, [list(range(3))]),
...     ("take_if", Iter.take_if, [lambda x: x]),
...     ("filter", Iter.filter, [lambda x: x]),
...     ("map", Iter.map, [lambda x: x]),
...     ("starmap", Iter.starmap, [lambda x, y, z: (x + y, y + z, z + x)]),
...     ("reversed", Iter.reversed, []),
...     ("sorted", Iter.sorted, []),
...     ("zip", Iter.zip, [list(range(4))]),
...     ("split", Iter.split, [4], lambda x: [list(x) for x in x]),
...     ("insert", Iter.insert, [2, "I AM HERE"]),
...     ("index", Iter.index, [[15, 16, 17]]),
... ):
...     lst = [list(range(i * 3, (i + 1) * 3)) for i in range(10)]
...     it1 = Iter(lst)
...     y0 = method(it1.copy().slice(2, None), *args).slice(10) / list
...     for post in postprocessings:
...         y0 = post(y0)
...     it2 = method(it1, *args)
...     _ = it1.slice(0, 2).now()
...     y1 = it2.slice(10) / list
...     for post in postprocessings:
...         y1 = post(y1)
...     if y0 != y1:
...         print(f"{name}{args} failed!")
...         print(y0)
...         print(y1)

```