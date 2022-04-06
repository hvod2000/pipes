import inspect
import itertools
import generators


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


def lazy(f, *args, **kwargs):
    yield from f(*args, **kwargs)


def generator(f):
    return lambda *args, **kwargs: Iter(f(*args, **kwargs))


# itertools functionality
Iter.accumulate = generator(itertools.accumulate)
Iter.chain = generator(generators.chain)
Iter.combinations = generator(generators.combinations)
Iter.combinations_with_repetition = generator(
    generators.combinations_with_repetition
)
Iter.combinations_with_replacement = generator(
    generators.combinations_with_repetition
)
Iter.compress = generator(itertools.compress)
Iter.cycle = generator(itertools.cycle)
Iter.skip_while = generator(generators.skip_while)
Iter.skip_if = generator(generators.skip)
Iter.group_by = generator(generators.group_by)
Iter.slice = generator(itertools.islice)
Iter.permutations = generator(generators.permutations)
Iter.permutations_with_repetition = generator(
    generators.permutations_with_repetition
)
Iter.product = generator(generators.product)
Iter.take_while = generator(generators.take_while)
Iter.duplicate = generator(itertools.tee)
Iter.zip_longest = generator(itertools.zip_longest)

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
    doctest.testfile(module_name + ".tests.md")
