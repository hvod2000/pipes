import inspect
import builtins
import itertools
import myitertools


class Iter:
    def __init__(self, iterator):
        self.iterator = iter(iterator)

    def apply(self, f, *args, **kwargs):
        return Iter(f(self.iterator, *args, **kwargs))

    def copy(self):
        self.iterator, new_iter = itertools.tee(self)
        return Iter(new_iter)

    def now(self):
        return Iter(list(self.iterator))

    def __truediv__(self, f):
        return f(self.iterator)

    def __getattr__(self, name):
        frame = inspect.currentframe()
        f = frame.f_back.f_locals.get(name, None)
        del frame
        return lambda *args, **kwargs: Iter(f(self.iterator, *args, **kwargs))

    def __iter__(self):
        return self.iterator

    def __next__(self):
        return next(self.iterator)


def generator(f):
    return lambda *args, **kwargs: Iter(f(*args, **kwargs))


# itertools functionality
Iter.accumulate = generator(itertools.accumulate)
Iter.chain = generator(myitertools.chain)
Iter.combinations = generator(itertools.combinations)
Iter.combinations_with_repetition = generator(itertools.combinations_with_replacement)
Iter.combinations_with_replacement = generator(itertools.combinations_with_replacement)
Iter.compress = generator(itertools.compress)
Iter.cycle = generator(itertools.cycle)
Iter.skip_while = generator(myitertools.skip_while)
Iter.skip_if = generator(myitertools.skip_if)
Iter.group_by = generator(itertools.groupby)
Iter.slice = generator(itertools.islice)
Iter.permutations = generator(itertools.permutations)
Iter.permutations_with_repetition = generator(itertools.product)
Iter.product = generator(itertools.product)
Iter.take_while = generator(itertools.takewhile)
Iter.tee = generator(itertools.tee)
Iter.zip_longest = generator(itertools.zip_longest)

# builtins functionality
Iter.take_if = lambda self, f: Iter(filter(f, self.iterator))
Iter.filter = Iter.take_if
Iter.map = lambda self, f: Iter(map(f, self.iterator))
Iter.starmap = lambda self, f: self.map(lambda args: f(*args))
Iter.reversed = generator(builtins.reversed)
Iter.sorted = generator(builtins.sorted)
Iter.zip = generator(builtins.zip)

if __name__ == "__main__":

    def myfunction(iterable, default=None):
        last_two = (default, default)
        for item in iterable:
            last_two = (last_two[-1], item)
        return last_two

    from math import isqrt

    test1 = (
        Iter(range(1, 11))
        .map(lambda x: x ** 2)
        .myfunction(default=0)
        .map(lambda x: isqrt(x))
        / list
    )
    print(test1)
    assert test1 == [9, 10]
