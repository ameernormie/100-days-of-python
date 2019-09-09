number = 5

if number == 5:
    print('number is five')
else:
    print('number is not five')


# List
array = []

if array:
    print('array is truthy or not empty')
else:
    print('array is falsy or empty')


# Not if
if number is not 5:
    print('number is not 5')
else:
    print('number is five')

# Ternary if statements
a = 1
b = 2

big = "bigger" if a > b else "smaller"
print(big)
