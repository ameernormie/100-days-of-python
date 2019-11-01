"""Decorators modify or enchance functions without chaning
their definition

Implemented as callables that take and return other callables
"""


def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)

    return wrap


@escape_unicode
def northern_city():
    return 'islæmábàd'


print(northern_city())
