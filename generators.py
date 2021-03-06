import itertools
import operator
import builtins
import collections


def product(*iterables, repeat=1):
    yield from itertools.product(*iterables, repeat=repeat)


def permutations(iterable, r=None):
    yield from itertools.permutations(iterable, r)


def permutations_with_repetition(iterable, size=None):
    lst = list(iterable)
    size = size if size is not None else len(lst)
    yield from itertools.product(lst, repeat=size)


def combinations(iterable, size=None):
    lst = list(iterable)
    size = size if size is not None else len(lst)
    yield from itertools.combinations(lst, size)


def combinations_with_repetition(iterable, size=None):
    lst = list(iterable)
    size = size if size is not None else len(lst)
    yield from itertools.combinations_with_replacement(lst, size)


def accumulate(iterable, func=operator.add, initial=None):
    return itertools.accumulate(iterable, func, initial=initial)


def chain(iterable, *iterables):
    if not len(iterables):
        return itertools.chain.from_iterable(iterable)
    return itertools.chain(iterable, *iterables)


def count(iterable, *xs):
    if len(xs):
        def count_items(iterable, *xs):
            counted = {x: 0 for x in xs}
            for item in iterable:
                if item in counted:
                    counted[item] += 1
            return counted
        yield from count_items(iterable, *xs).items()
        return
    yield from collections.Counter(iterable).items()


def skip_while(iterable, predicate):
    return itertools.dropwhile(predicate, iterable)


def skip(iterable, condition):
    match condition:
        case predicate if callable(predicate):
            return itertools.filterfalse(predicate, iterable)
        case int(size):
            return itertools.islice(iterable, size, None)
        case mask:
            return itertools.compress(iterable, (not b for b in mask))


def take_while(iterable, predicate):
    return itertools.takewhile(predicate, iterable)


def take(iterable, condition):
    match condition:
        case predicate if callable(predicate):
            return builtins.filter(predicate, iterable)
        case int(size):
            return itertools.islice(iterable, size)
        case mask:
            return itertools.compress(iterable, mask)


def group_by(iterable, key=None):
    for key, group in itertools.groupby(iterable, key):
        yield (key, tuple(group))


def zip(iterable, *other_iterables):
    if other_iterables:
        return builtins.zip(iterable, *other_iterables)
    return builtins.zip(*iterable)


def zip_longest(iterable, *other_iterables):
    if other_iterables:
        return itertools.zip_longest(iterable, *other_iterables)
    return itertools.zip_longest(*iterable)


def reversed(iterable, key=None):
    yield from builtins.reversed(list(iterable))


def sorted(iterable, key=None):
    yield from builtins.sorted(list(iterable))


def slice(iterable, *args):
    match args:
        case [end]:
            yield from (itertools.islice(iterable, None, end, 1))
        case [start, end]:
            yield from (itertools.islice(iterable, start, end, 1))
        case [start, end, step]:
            yield from (itertools.islice(iterable, start, end, step))
        case _:
            raise ValueError()


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


def cycle(iterable):
    return itertools.cycle(iterable)
