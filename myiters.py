import inspect


class Iter:
    def __init__(self, iterator):
        self.iterator = iterator

    def filter(self, f):
        return Iter(filter(f, self.iterator))

    def map(self, f):
        return Iter(map(f, self.iterator))

    def __getattr__(self, name):
        frame = inspect.currentframe()
        f = frame.f_back.f_locals.get(name, None)
        del frame
        return lambda *args, **kwargs: Iter(f(self.iterator, *args, **kwargs))

    def __iter__(self):
        yield from self.iterator


if __name__ == "__main__":

    def myfunction(iterable, default=None):
        last_two = (default, default)
        for item in iterable:
            last_two = (last_two[-1], item)
        return last_two

    from math import isqrt

    test1 = list(
        Iter(range(1, 11))
        .map(lambda x: x ** 2)
        .myfunction(default=0)
        .map(lambda x: isqrt(x))
    )
    print(test1)
    assert test1 == [9, 10]
