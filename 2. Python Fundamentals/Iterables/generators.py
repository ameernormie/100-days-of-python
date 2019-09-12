"""Generators in Python are normal functions with atleast one yield statement in them

They stop executing at yield. 
Generators are iterables so we can iterate over them to get values

Generators can maintain state in local variables
Lazy evaluation
"""


def gen123():
    yield 1
    yield 2
    yield 3


g = gen123()
g               # <generator object gen123 at 0x1005d94d0>

next(g)      # 1
next(g)      # 2
next(g)      # 3
next(g)      # Exception:  StopIteration
