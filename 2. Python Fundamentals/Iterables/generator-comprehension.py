"""Generator Comprehensions

Similar syntax to list comprehensions
Create a generator object
Concise
Lazy Evaluation

"""

million_squares = (x*x for x in range(1, 1000001))

""" This returned us a generator function that can be lazily consumed"""
million_squares         # <generator object <genexpr> at 0x1005d9550>


"""To evaluate the generator"""
# list(million_squares)


"""Calculate the sum of first 10 million squares using the built-in sum"""
sum(x*x for x in range(1, 10000001))

# generators
