import inspect


class Iter:
    def __init__(self, iterator):
        self.iterator = iterator

    def filter(self, f):
        return Iter(filter(f, self.iterator))

    def map(self, f):
        return Iter(map(f, self.iterator))

    def __iter__(self):
        yield from self.iterator
