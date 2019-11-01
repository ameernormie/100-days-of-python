"""A practical use of decorators is validating function arguments"""


# <==== Not a decorator but a function that returns decorator
def check_non_negative(index):
    """ This is not a decorator but a simple function. 
    Decorators take and return a callable method.
    So, this function returns a decorator in its return"""
    def validator(f):
        def wrap(*args):
            if args[index] < 0:
                raise ValueError(
                    'Argument {} must be non-negative.'.format(index)
                )
            return f(*args)
        return wrap
    return validator


@check_non_negative(1)
def create_list(value, size):
    return [value] * size


create_list(2, 0)           # []
create_list(2, 3)           # [2, 2, 2]


# the following will raise value error because of decorator
create_list(2, -1)          # ValueError: Argument 1 must be non-negative.
