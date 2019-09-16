"""
Given an array X of 0s and 1s, divide the array in to 3 non empty parts 
such that all of these parts represent the same binary value

If it is possible, return any i, j such that
* Z[0], Z[1], ... , Z[i] is the first part;
* Z[i+1], Z[i+2], ... , Z[j - 1] is the second part;
* Z[j], Z[j + 1], ... , Z[Z.lenght -1] is the first part;

If it is not possible, return [-1, -1]

Example 1:
Input: [1, 0, 1, 0, 1]
Output: [0, 3]

Example 2:
Input: [1, 1, 0, 1, 1]
Output: [-1, -1]
"""


def return_three_segs(input, divider):
    return input[:divider], input[divider: divider*2], input[divider*2:]


def divide(input):
    manipulated_array = False
    if len(input) % 3 is 2:
        manipulated_array = True
        input = [0] + input
    elif len(input) % 3 is 1:
        return [-1, -1]
    else:
        pass
    one, two, three = return_three_segs(input, len(input)//3)
    print('one two three ', one, two, three)
    if one == two == three:
        return [0, (len(input)//3 * 2) - 1 if manipulated_array else len(input)//3 * 2]
    else:
        return [-1, -1]
