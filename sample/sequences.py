#!/usr/bin/env python3

'''
Mathematical sequences
'''

from itertools import count

def fib(a=1, b=1):
    '''
    fibonacci sequence

    :param a: starting value for a
    :param b: starting value for b

    >>> from itertools import islice
    >>> f = fib()
    >>> list(islice(f, 10))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    '''
    while True:
        yield a
        a, b = b, a+b

def collatz(n):
    '''
    collatz conjecture sequence

    >>> from itertools import takewhile
    >>> c = collatz(10)
    >>> next(c)
    10
    >>> list(takewhile(lambda x: x != 1, c))
    [5.0, 16.0, 8.0, 4.0, 2.0]
    '''
    while True:
        yield n
        n = 3 * n + 1 if n % 2 else n / 2

def square():
    '''
    sequence of squares
    '''
    for x in count():
        yield x ** 2

def triangle():
    '''
    sequence of triangle numbers
    '''
    for x in count():
        yield x * (x + 1) / 2

if __name__ == '__main__':
    import doctest
    doctest.testmod()
