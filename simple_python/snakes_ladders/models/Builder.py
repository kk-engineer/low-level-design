def builder(func):
    def wrapper(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self

    return wrapper
