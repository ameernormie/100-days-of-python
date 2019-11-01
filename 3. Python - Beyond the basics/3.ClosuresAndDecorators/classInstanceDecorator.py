class Trace:
    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print('Calling {}'.format(f))
            return f(*args, **kwargs)
        return wrap


tracer = Trace()

"""This decorator is on the instance of Trace class"""
@tracer
def rotate_list(l):
    return l[1:] + [l[0]]


l = [1, 2, 3]

l = rotate_list(l)          # Calling <function rotate_list at 0x11032d200>
print(l)                    # [2, 3, 1]
l = rotate_list(l)          # Calling <function rotate_list at 0x11032d200>
print(l)                    # [3, 1, 2]
l = rotate_list(l)          # Calling <function rotate_list at 0x11032d200>
print(l)                    # [1, 2, 3]

print('disabling tracer')
# disabling tracer - After this decorator will not trace the function
tracer.enabled = False

l = rotate_list(l)
print(l)
