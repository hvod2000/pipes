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
