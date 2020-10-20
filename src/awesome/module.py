from .version import __version__

def hello():
    """Say hello!

    This function says hello and reports the current version of this package.
    """
    return ('Hello, my newest version is ' + __version__)

def add(x, y):
    """Add things!
    Function to add things.

    :param x: first number
    :type x: float

    :param y: second number
    :type y: float

    :return: addition of x and y
    :rtype: float

    >>> add(1, 1)
    2
    """
    return (float(x) + float(y))


def add_cmd():
    """command line wrapper for add function"""
    import sys
    arg1, arg2 = sys.argv[1], sys.argv[2]
    print("Hello friend! " + arg1 + " + " + arg2 + " = " + str(add(arg1, arg2)))
