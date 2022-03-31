from functools import update_wrapper


class Pipe:
    def __init__(self, function):
        self.function = function
        update_wrapper(self, function)

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)

    def __ror__(self, arg):
        return self(arg)


class PipeWithKwargs(Pipe):
    def __init__(self, function, kwargs=None):
        self.kwargs = {} if kwargs is None else kwargs
        super().__init__(function)

    def __call__(self, *args, **kwargs):
        kwargs = self.kwargs | kwargs
        if len(args):
            return self.function(*args, **kwargs)
        return PipeWithKwargs(self.function, kwargs)


class PipeWithArgs(PipeWithKwargs):
    def __init__(self, function, args_len, args_preprocessing=None, args=None):
        self.args_len = args_len
        self.args_preproc = args_preprocessing
        self.args, kwargs = ((), {}) if args is None else args
        super().__init__(function, kwargs)

    def __call__(self, *args, **kwargs):
        args = self.args + args
        kwargs = self.kwargs | kwargs
        fun, args_len = self.function, self.args_len
        if len(args) >= args_len:
            return fun(*args, **kwargs)
        return PipeWithArgs(fun, args_len, self.args_preproc, (args, kwargs))

    def __ror__(self, arg):
        if self.args_preproc is not None:
            args = self.args_preproc(arg, *self.args)
            return self.function(*args, **self.kwargs)
        return self.function(arg, *self.args, **self.kwargs)


def pipize(*args):
    match args:
        case f, args_size, args_preprocessor:
            if args_size == 1:
                if f.__code__.co_kwonlyargcount + len(f.__defaults__ or ()):
                    return PipeWithKwargs(f)
                return Pipe(f)
            return PipeWithArgs(f, args_size, args_preprocessor)
        case int(args_size), args_preprocessor:
            return lambda f: pipize(f, args_size, args_preprocessor)
        case f, int(args_size):
            return pipize(f, args_size, None)
        case int(args_size),:
            return lambda f: pipize(f, args_size, None)
        case f,:
            args_size = f.__code__.co_argcount - len(f.__defaults__ or ())
            return pipize(f, args_size, None)
