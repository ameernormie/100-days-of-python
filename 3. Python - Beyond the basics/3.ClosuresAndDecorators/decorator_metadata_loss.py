"""
By adding a decorator to a method we lose the name 
and doc of the method that we get by __name__ and __doc__ 
method. This could cause trouble if we want to check these things
"""


def noop(f):
    def noop_wrapper():
        return f()

    noop_wrapper.__name__ = f.__name__
    noop_wrapper.__doc__ = f.__doc__
    return noop_wrapper


@noop
def hello():
    "Print a most commonly used string"
    print('Hello world')
