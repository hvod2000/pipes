from functools import update_wrapper


class Pipe:
    def __init__(self, function, kwargs=None):
        self.function = function
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        return Pipe(self.function, *args, **kwargs)

    def __ror__(self, other):
        return self.function(other)
