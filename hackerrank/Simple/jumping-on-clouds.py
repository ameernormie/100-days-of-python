#!/bin/python3
"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
She can jump on any cumulus cloud having a number that is equal to the number of the
current cloud plus  or . She must avoid the thunderheads.
Determine the minimum number of jumps it will take Emma to jump from her starting position
to the last cloud. It is always possible to win the game.
For each game, Emma will get an array of clouds numbered  if they are safe or
if they must be avoided. For example,  indexed from .
The number on each cloud is its index in the list so she must avoid the clouds at indexes  and .
She could follow the following two paths:  or . The first path takes  jumps while the second takes .
"""


def jumpingOnClouds(c):
    """
    Args:
        c: an array of binary integers

    Returns:
        minimum number of jumps required, as an integer
    """
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 0 if c[1] == 1 else 1
    if c[2] == 1:
        return 1 + jumpingOnClouds(c[1:])
    if c[2] == 0:
        return 1 + jumpingOnClouds(c[2:])


def get_jumps():
    jumps = jumpingOnClouds([0, 0, 0, 0, 0, 1, 0, 0, 1])
    print(jumps)


if __name__ == '__main__':
    get_jumps()
