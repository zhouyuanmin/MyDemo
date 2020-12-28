def print_copy(func):
    def wrapper(*args, **kwargs):
        kwargs['flush'] = True
        kwargs['end'] = '*'
        return func(*args, **kwargs)
    return wrapper


print = print_copy(print)