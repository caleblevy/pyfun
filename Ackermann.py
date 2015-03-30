#!/usr/bin/env python

"""Representation of the Ackermann function in python.

Caleb Levy, 2014.
"""


def Ackermann(m, n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return Ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return Ackermann(m-1, Ackermann(m, n-1))


if __name__ == '__main__':
    assert Ackermann(3, 3) == 61
