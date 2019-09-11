range(5)        # range(0,5)

range(5, 10)

list(range(5, 10))  # [5, 6, 7, 8, 9]

list(range(0, 10, 2))   # [0, 2, 4, 6, 8]

# Counter
t = [6, 10, 12, 14, 14]
for p in enumerate(t):
    print(p)

# (0, 6)
# (1, 10)
# (2, 12)
# (3, 14)
# (4, 14)


for i, v in enumerate(t):
    print("i = {}, v = {}".format(i, v))

# i = 0, v = 6
# i = 1, v = 10
# i = 2, v = 12
# i = 3, v = 14
# i = 4, v = 14
