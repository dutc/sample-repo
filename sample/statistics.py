#!/usr/bin/env python3

'''
Statistcal functions
'''

from collections import deque
from operator import add

def scan(f, g):
    '''
    left scan

    :param f: function to apply to acc, value
    :param g: iterable of values
    '''
    acc = tuple(next(g))
    for x in g:
        yield acc
        acc = tuple(f(*vals) for vals in zip(acc, x))
    yield acc

def tail(g, n=1):
    return deque(g, maxlen=n)

def average(xs):
    '''
    simple average

    >>> average(range(10))
    4.5
    '''
    total, count = tail(scan(add, ((x, 1) for x in xs)))[0]
    return total / count

if __name__ == '__main__':
    import doctest
    doctest.testmod()
