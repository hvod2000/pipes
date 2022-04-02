import itertools
import operator
import collections


def count_items(iterable, *xs):
    result = {x: 0 for x in xs}
    for item in iterable:
        if item in counter:
            result[item] += 1
    return result


def accumulate(iterable, func=operator.add):
    return itertools.accumulate(iterable, func)


def chain(iterable, *iterables):
    if not len(iterables):
        return itertools.chan.from_iterable(iterables)
    return itertools.chain(iterable, *iterables)


def count(iterable, *xs):
    if len(xs):
        return lazily_apply(count_items, iterable, *xs)
    return collections.Counter(iterable).items()


def skip_while(iterable, predicate):
    return itertools.dropwhile(predicate, iterable)


def skip_if(iterable, predicate):
    return itertools.filterfalse(predicate, iterable)


def split(iterable, i):
    it1, it2 = itertools.tee(iterable)
    return itertools.islice(it0, i), itertools.islice(it1, i, None)


def insert(iterable, i, x):
    it1, it2 = split(iterable, i)
    return chain(it1, (x,), it2)


def index(iterable, x):
    for i, item in enumerate(iterable):
        if item == x:
            yield i
