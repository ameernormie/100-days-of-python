"""
Basic idea of dictionaries in python
Key-value pair

Keys must be immutable i.e. strings, numbers and tuples
Values can be mutable 

Never rely on order of items in the dictionary
"""

# Make from other iterables
names_and_ages = [('Alice', 32), ('Ameer', 25), ('Bob', 45)]
d = dict(names_and_ages)
d                   # {'Alice': 32, 'Ameer': 25, 'Bob': 45}


phonetic = dict(a='alpha', b='beta', c='charlie', d='delta')
phonetic            # {'a': 'alpha', 'b': 'beta', 'c': 'charlie', 'd': 'delta'}


# Copying
d = {'key': 'value'}
c = d.copy()

another_copy = dict(d)

# Extend dictionary
g = dict(wheat='231233')
c.update(g)

# Iteration

d = {'a': 1, 'b': 2}

for k in d:
    print('key {} and value {}'.format(k, d[k]))

for value in d.values():
    print('values')

for key in d.keys():
    print('keys')

for key, value in d.items():
    print('key and value')


# membership        in and not in operator
