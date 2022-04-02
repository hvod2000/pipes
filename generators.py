import itertools
import operator
import builtins
import collections


def count_items(iterable, *xs):
    result = {x: 0 for x in xs}
    for item in iterable:
        if item in counter:
            result[item] += 1
    return result


def permutations_with_repetition(iterable, r):
    return itertools.product(iterable, repeat=r)


def accumulate(iterable, func=operator.add):
    return itertools.accumulate(iterable, func)


def chain(iterable, *iterables):
    if not len(iterables):
        return itertools.chain.from_iterable(iterable)
    return itertools.chain(iterable, *iterables)


def count(iterable, *xs):
    if len(xs):
        return lazily_apply(count_items, iterable, *xs)
    return collections.Counter(iterable).items()


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
    return itertools.islice(it1, i), itertools.islice(it2, i, None)


def insert(iterable, i, x):
    it1, it2 = split(iterable, i)
    return chain(it1, (x,), it2)


def index(iterable, x):
    for i, item in enumerate(iterable):
        if item == x:
            yield i
