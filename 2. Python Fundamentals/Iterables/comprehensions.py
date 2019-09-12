from math import factorial, sqrt
from pprint import pprint as pp

words = "Why sometimes I have believed as many as six impossible things before breakfast".split(
    " ")

'''['Why', 'sometimes', 'I', 'have', 'believed', 'as', 'many', 'as', 'six', 'impossible', 'things', 'before', 'breakfast']'''

"""List Comprehension"""
[len(word) for word in words]
# [3, 9, 1, 4, 8, 2, 4, 2, 3, 10, 6, 6, 9]

[len(str(factorial(x))) for x in range(20)]
# [1, 1, 1, 1, 2, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18]


"""Sets Comprehension"""
{len(str(factorial(x))) for x in range(20)}
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18}


"""Dictionary Comprehension"""
country_to_capital = {'United Kingdom': 'London',
                      'Brazil': 'Brazilia',
                      'Morocco': 'Rabat',
                      'Pakistan': 'Islamabad'}

capital_to_country = {capital: country for country,
                      capital in country_to_capital.items()}

capital_to_country
"""
{'Brazilia': 'Brazil',
 'Islamabad': 'Pakistan',
 'London': 'United Kingdom',
 'Rabat': 'Morocco'}
"""


def is_prime(x):
    if(x < 2):
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


"""Filtering Predicates

[expr(item) for item in iterable if predicate(item)]
"""

[x for x in range(101) if is_prime(x)]
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

prime_square_divisors = {x*x: (1, x, x*x) for x in range(101) if is_prime(x)}

"""
{4: (1, 2, 4),
 9: (1, 3, 9),
 25: (1, 5, 25),
 49: (1, 7, 49),
 121: (1, 11, 121),
 169: (1, 13, 169),
 289: (1, 17, 289),
 361: (1, 19, 361),
 529: (1, 23, 529),
 841: (1, 29, 841),
 961: (1, 31, 961),
 1369: (1, 37, 1369),
 1681: (1, 41, 1681),
 1849: (1, 43, 1849),
 2209: (1, 47, 2209),
 2809: (1, 53, 2809),
 3481: (1, 59, 3481),
 3721: (1, 61, 3721),
 4489: (1, 67, 4489),
 5041: (1, 71, 5041),
 5329: (1, 73, 5329),
 6241: (1, 79, 6241),
 6889: (1, 83, 6889),
 7921: (1, 89, 7921),
 9409: (1, 97, 9409)}
"""
