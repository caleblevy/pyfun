#!/usr/bin/env Python

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

print Ackermann(3, 3)
