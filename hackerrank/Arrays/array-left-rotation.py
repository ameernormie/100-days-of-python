"""A left rotation operation on an array shifts each of the array's elements unit to the left
"""


def rotateLeft(a, rot):
    """Rotates the array to left 

    Args:
        a: list to rotate
        rot: number of times to rotate

    Returns:
        Rotated list
    """
    return a[rot:]+a[:rot]


def run_rotate():
    a = [1, 2, 3, 4, 5]
    rotated_list = rotateLeft(a, 4)
    print(rotated_list)


if __name__ == '__main__':
    run_rotate()
