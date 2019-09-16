#!/usr/bin/env python3
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
    """ Divides the input in three equal segments based on the divider

    Returns:
        A tuple of three segments
    """
    return input[:divider], input[divider: divider*2], input[divider*2:]


def equal_binaries(input):
    """ Determines if the input has equal binary values if it's divided in 3 parts

    Args:
        input: list stream of binaries

    Returns:
        index of first and third segment in list if equal binary values exist otherwise [-1,-1]
    """
    manipulated_array = False
    if not input or len(input) < 3:
        return [-1, -1]
    if len(input) % 3 is 2:
        manipulated_array = True
        input = [0] + input
    elif len(input) % 3 is 1:
        return [-1, -1]
    else:
        pass
    one, two, three = return_three_segs(input, len(input)//3)
    if one == two == three:
        return [0, (len(input)//3 * 2) - 1 if manipulated_array else len(input)//3 * 2]
    else:
        return [-1, -1]


def run_binary_equals():
    input_one = [1, 0, 1, 0, 1]
    input_two = [1, 1, 0, 1, 1]

    print(equal_binaries(input_one))
    print(equal_binaries(input_two))


if __name__ == '__main__':
    run_binary_equals()
