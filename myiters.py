import inspect
import itertools
import functools
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
        if f is None:
            raise NameError(f"function {name}() is not defined")
        return lambda *args, **kwargs: Iter(f(self.iterator, *args, **kwargs))

    def __iter__(self):
        return self.iterator

    def __next__(self):
        return next(self.iterator)

    @classmethod
    def add_method(cls, f):
        m = functools.wraps(f)(lambda *args, **kwargs: Iter(f(*args, **kwargs)))
        if hasattr(cls, f.__name__):
            raise NameError(f"method {f.__name__}() is already defined")
        setattr(cls, f.__name__, m)


Iter.map = lambda self, f: Iter(map(f, self.iterator))
Iter.starmap = lambda self, f: Iter(map(lambda args: f(*args), self.iterator))
for name, f in generators.__dict__.items():
    if callable(f):
        Iter.add_method(f)
Iter.split = lambda *args: Iter(map(Iter, generators.split(*args)))

if __name__ == "__main__":
    import doctest

    module_name = __file__.split("/")[-1].removesuffix(".py")
    doctest.testfile(module_name + ".md")
