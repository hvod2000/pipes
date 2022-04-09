import inspect
import itertools
import generators


class Iter:
    def __init__(self, iterator):
        self.iterator = iter(iterator)

    def apply(self, f, *args, **kwargs):
        return Iter(f(self.iterator, *args, **kwargs))

    def copy(self, n=None):
        if n is None:
            self.iterator, new_iter = itertools.tee(self)
            return Iter(new_iter)
        return Iter(map(Iter, itertools.tee(self, n)))

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


def lazy(f, *args, **kwargs):
    yield from f(*args, **kwargs)


def generator(f):
    return lambda *args, **kwargs: Iter(f(*args, **kwargs))


# itertools functionality
Iter.accumulate = generator(generators.accumulate)
Iter.chain = generator(generators.chain)
Iter.combinations = generator(generators.combinations)
Iter.combinations_with_repetition = generator(
    generators.combinations_with_repetition
)
Iter.combinations_with_replacement = generator(
    generators.combinations_with_repetition
)
Iter.compress = generator(generators.take)
Iter.cycle = generator(generators.cycle)
Iter.skip_while = generator(generators.skip_while)
Iter.skip_if = generator(generators.skip)
Iter.group_by = generator(generators.group_by)
Iter.slice = generator(generators.slice)
Iter.permutations = generator(generators.permutations)
Iter.permutations_with_repetition = generator(
    generators.permutations_with_repetition
)
Iter.product = generator(generators.product)
Iter.take_while = generator(generators.take_while)
Iter.zip_longest = generator(generators.zip_longest)

# builtins functionality
Iter.take_if = lambda self, f: Iter(filter(f, self.iterator))
Iter.filter = Iter.take_if
Iter.map = lambda self, f: Iter(map(f, self.iterator))
Iter.starmap = lambda self, f: self.map(lambda args: f(*args))
Iter.reversed = generator(generators.reversed)
Iter.sorted = generator(generators.sorted)
Iter.zip = generator(generators.zip)

# list functionality
Iter.split = lambda *args: Iter(map(Iter, generators.split(*args)))
Iter.insert = generator(generators.insert)
Iter.index = generator(generators.index)

if __name__ == "__main__":
    import doctest

    module_name = __file__.split("/")[-1].removesuffix(".py")
    doctest.testfile(module_name + ".md")
