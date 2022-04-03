import itertools
import operator
import builtins
import collections


def count_items(iterable, *xs):
    result = {x: 0 for x in xs}
    for item in iterable:
        if item in result:
            result[item] += 1
    return result


def product(*iterables, repeat=1):
    yield from itertools.product(*iterables, repeat=repeat)


def permutations(iterable, r=None):
    yield from itertools.permutations(iterable, r)


def permutations_with_repetition(iterable, r=None):
    if r is not None:
        yield from itertools.product(iterable, repeat=r)
        return
    lst = list(iterable)
    yield from itertools.product(lst, repeat=len(lst))


def combinations(iterable, r=None):
    if r is not None:
        yield from itertools.combinations(iterable, r)
    else:
        yield from (tuple(iterable) for _ in range(1))


def combinations_with_repetition(iterable, r=None):
    if r is not None:
        yield from itertools.combinations_with_replacement(iterable, r)
        return
    lst = list(iterable)
    yield from itertools.combinations_with_replacement(lst, len(lst))


def accumulate(iterable, func=operator.add):
    return itertools.accumulate(iterable, func)


def chain(iterable, *iterables):
    if not len(iterables):
        return itertools.chain.from_iterable(iterable)
    return itertools.chain(iterable, *iterables)


def count(iterable, *xs):
    if len(xs):
        counted = count_items(iterable, *xs)
        yield from counted.items()
        return
    yield from collections.Counter(iterable).items()


def skip_while(iterable, predicate):
    return itertools.dropwhile(predicate, iterable)


def skip_if(iterable, predicate):
    return itertools.filterfalse(predicate, iterable)


def take_while(iterable, predicate):
    return itertools.takewhile(predicate, iterable)


def group_by(iterable, key=None):
    for key, group in itertools.groupby(iterable, key):
        yield (key, tuple(group))


def zip(iterable, *other_iterables):
    if other_iterables:
        return builtins.zip(iterable, *other_iterables)
    return builtins.zip(*iterable)


def reversed(iterable, key=None):
    yield from builtins.reversed(list(iterable))


def sorted(iterable, key=None):
    yield from builtins.reversed(list(iterable))


def split(iterable, i):
    it1, it2 = itertools.tee(iterable)
    yield from (itertools.islice(it1, i), itertools.islice(it2, i, None))


def insert(iterable, i, x):
    it1, it2 = split(iterable, i)
    yield from chain(it1, (x,), it2)


def index(iterable, x):
    for i, item in enumerate(iterable):
        if item == x:
            yield i
