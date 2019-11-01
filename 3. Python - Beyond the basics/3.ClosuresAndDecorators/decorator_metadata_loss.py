"""
By adding a decorator to a method we lose the name 
and doc of the method that we get by __name__ and __doc__ 
method. This could cause trouble if we want to check these things
"""

import functools


def noop(f):
    @functools.wraps(f)
    def noop_wrapper():
        return f()
    return noop_wrapper


@noop
def hello():
    "Print a most commonly used string"
    print('Hello world')
