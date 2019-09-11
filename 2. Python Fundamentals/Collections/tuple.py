# Immutable

t = (1, 2, 3, "123")

# Concatenation
t + (4, 5)           # (1, 2, 3, "123", 4, 5)

t                    # (1, 2, 3, "123")

# Single value tuple is different
t = (123)       # Will be recognized as a int
type(t)         # <class 'int'>

# Append a comma for a single value tuple
t = (123,)
type(t)         # <class 'tuple'>

# Empty tuple is simple
t = ()


# Tuples are useful in multi return values
def minmax(items):
    return min(items), max(items)


minmax([1, 2, 3, 4, 5, 6, 7])         # (1, 7)

# Tuple unpacking

lower, upper = minmax([1, 2, 3, 4, 5, 6, 7])

lower           # 1
upper           # 7

# Tuple unpacking works with arbirarily nested tuples
(a, (b, (c, d))) = (4, (3, (2, 1)))

a       # 4
b       # 3
c       # 2
d       # 1


# Swapping
a, b = b, a

# Create a tuple from existing collection
tuple(['a', 'b', 'c'])          # ('a', 'b', 'c')
tuple('ameer')                  # ('a', 'm', 'e', 'e', 'r')

# Check membership
5 in (5, 6, 7, 7)               # True
