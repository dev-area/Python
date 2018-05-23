
def f1():
    print ('f1')


def f2(a, b):
    """
    great function
    >>> f2(2,3)
    5
    >>> f2(4,8)
    12
    >>> f2(23,45)
    68
    >>> f2(33,-100)
    -67
    """
    return a + b


if __name__ == '__main__':
    import doctest

    doctest.testmod()
