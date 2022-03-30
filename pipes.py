from functools import update_wrapper


class Pipe:
    def __init__(self, function, kwargs=None):
        self.function = function
        self.kwargs = kwargs or {}
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        kwargs = kwargs | self.kwargs
        if len(args):
            return args | Pipe(self.function, kwargs)
        return Pipe(self.function, kwargs)

    def __ror__(self, other):
        return self.function(other, **self.kwargs)
