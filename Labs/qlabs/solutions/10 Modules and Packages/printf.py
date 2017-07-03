#!/usr/bin/python
"""
    This module supplies functions sprintf, fprintf,
    and printf.
    
    >>> printf("%s","hello")
    hello
    >>> printf("%x",42)
    2a
    >>> printf("|%06.2f %-12s|",3.1426,"hello")
    |003.14 hello       |
    >>> var = sprintf("%X",3735928559)
    >>> print(var)
    DEADBEEF
"""
import sys

def sprintf(fmt, *args):
    rstr = fmt % args
    return rstr

def fprintf(file, fmt, *args):
    file.write(sprintf(fmt, *args))
    
def printf(fmt, *args):
    fprintf(sys.stdout,fmt,*args)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    