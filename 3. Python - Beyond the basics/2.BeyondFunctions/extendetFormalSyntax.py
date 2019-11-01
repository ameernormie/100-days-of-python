""" *args merges the random number of arguments into a tuple. 
we can use that tuple inside the function to do usefule things
*args ===> tuple

**kwargs is for random number of keyword arguments.
**kwargs is a dict object
"""


def hypervolume(*lengths):
    """Returns the volume of arbitrary number of arguments"""
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


# The above function will throw error if no arguments are passed to hypervolume


def hypervolumerevised(length, *lengths):
    """ This implementation makes sure that atlease one argument is
    required and that one argument will be used as the first value of the iteration
    """
    v = length
    for item in lengths:
        v *= item
    return v


""" **kwargs """


def tag(name, **kwargs):
    """Returns a tag with the name given by adding it's attributes to it"""
    result = '<' + name
    for key, value in kwargs.items():
        result += ' {k}="{v}"'.format(k=key, v=str(value))
    result += '>'
    return result


print(tag('img', src='monet.jpg', alt="Sunrise by claude van damme", border=1))
