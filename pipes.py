from functools import update_wrapper


class Pipe:
    def __init__(self, function, args_len=1, args_preproc=None, args=None):
        self.function = function
        self.args_len = args_len
        self.args_preprocessing = args_preproc
        self.args, self.kwargs = ((), {}) if args is None else args
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        preproc = self.args_preprocessing
        kwargs = self.kwargs | kwargs
        if len(args) + len(self.args) >= self.args_len:
            args = (args[0],) + self.args + args[1:]
            if self.args_preprocessing is not None:
                args = self.args_preprocessing(args)
            return self.function(*args, **kwargs)
        args = (self.args + args, kwargs)
        return Pipe(self.function, self.args_len, preproc, args)

    def __ror__(self, other):
        return self(other)
