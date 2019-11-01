def print_args(arg1, arg2, *args):
    print(arg1)
    print(arg2)
    print(args)


arguments = (1, 2, 3, 4, 5)

# Unpack a tuple to populate arguments of print_args
print_args(*arguments)

# 1
# 2
# (3, 4, 5)


def colors(red, green, blue, **kwargs):
    print("r =", red)
    print("g =", green)
    print("g =", blue)
    print(kwargs)


k = {'red': 21, 'green': 12, 'blue': 45, 'alpha': 0.7}
colors(**k)
