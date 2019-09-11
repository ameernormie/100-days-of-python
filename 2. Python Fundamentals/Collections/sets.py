p = {2, 3, 4, 5, 6}         # {2, 3, 4, 5, 6}

type(p)  # <class 'set'>

# Empty set
p = {}
type(p)     # <class 'dict'>

p = set()
type(p)     # <class 'set'>

"""Sets don't contain duplicates so they can be used to remove duplicates from collections"""

t = [1, 2, 1, 4, 3, 4, 5, 6, 3, 2, 4, 2]
set(t)          # {1, 2, 3, 4, 5, 6}


"""
Set Algebra
"""
blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
blond_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
smell_hydrogen = {'Harry', 'Amelia'}
taste_potassium = {'Harry', 'Lily', 'Amelia', 'Lola'}
o_blood = {'Mia', 'Lily', 'Joshua', 'Olivia'}
b_blood = {'Jack', 'Amelia'}
a_blood = {'Harry'}
ab_blood = {'Joshua', 'Lola'}


# {'Joshua', 'Jack', 'Amelia', 'Olivia', 'Lily', 'Mia', 'Harry'}
blue_eyes.union(blond_hair)

blond_hair.intersection(blue_eyes)      # {'Jack', 'Harry', 'Amelia'}

# difference
# symmetric_difference


"""Relationship between sets"""
# issubset
# issuperset
# isdisjoint
