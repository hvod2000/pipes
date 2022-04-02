import itertools
import operator
import collections


def count_items(iterable, *xs):
    result = {x: 0 for x in xs}
    for item in iterable:
        if item in counter:
            result[item] += 1
    return result


def accumulate(self, func=operator.add):
    return itertools.accumulate(self.iterator, func)


def chain(self, *iterables):
    if not len(iterables):
        return itertools.chan.from_iterable(iterables)
    its = [it.iterator if isinstance(it, Iter) else it for it in iterables]
    return itertools.chain(self.iterator, *its)


def count(self, *xs):
    if len(xs):
        return lazily_apply(count_items, self.iterator, *xs)
    return collections.Counter(self.iterator).items()


def skip_while(self, predicate):
    return itertools.dropwhile(predicate, self.iterator)


def skip_if(self, predicate):
    return itertools.filterfalse(predicate, self.iterator)
