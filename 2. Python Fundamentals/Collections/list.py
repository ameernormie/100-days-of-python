# slice

s = 'show how to index into sequences'.split()

s[1:4]          # ['how', 'to', 'index']

s[1:-1]     # ['how', 'to', 'index', 'into']

# Copying a list            Shallow copy
full_slice = s[:]
simple_copy = s.copy()
another_copy = list(s)          # Preffered


# Repitition
c = [21, 12]
d = c * 4

d       # [21,12,21,12,21,12,21,12]


# Finding elements
# ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
w = "the quick brown fox jumps over the lazy dog".split()

i = w.index('fox')          # 3

# Reversing
g = [1, 2, 3]
g.reverse       # [3,2,1]

# Sorting
s = [2, 3, 1]
s.sort()        # [1,2,3]

s.sort(reverse=True)        # [3,2,1]

# Sorting by key
h = "by performing the length operation of the turbine and i don't know what i am writing".split()
#['by', 'performing', 'the', 'length', 'operation', 'of', 'the', 'turbine', 'and', 'i', "don't", 'know', 'what', 'i', 'am', 'writing']

h.sort(key=len)
# ['i', 'i', 'by', 'of', 'am', 'the', 'the', 'and', 'know', 'what', "don't", 'length', 'turbine', 'writing', 'operation', 'performing']


# Sorted and reversed
x = [4, 9, 2, 67]
y = sorted(x)
y                   # [2, 4, 9, 67]

r = reversed(x)

r            # <list_reverseiterator object at 0x1044078d0>
list(r)         # [67, 2, 9, 4]
