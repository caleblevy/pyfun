#!/usr/bin/env python

"""Module for calculating sine and cosine function solely using parametrization
of unit circle by arc-length; i.e. no power series, no circular definitions in
terms of complex exponentials, and no right triangles.

Caleb Levy, March 2015.
"""

import numpy as np
import matplotlib.pyplot as plt


def circle_points(n):
    """Return n point approximation to the unit circle using the definition
    that (x, y) is on the unit circle if x**2 + y**2 = 1."""
    top = np.linspace(1, -1, n)[:-1]
    bottom = np.linspace(-1, 1, n)
    x = np.concatenate((top, bottom))
    circle_top = np.sqrt(1 - top**2)
    circle_bot = -np.sqrt(1 - bottom**2)
    y = np.concatenate((circle_top, circle_bot))
    return x, y


def arc_length(x, y):
    """Parametrize angle by arc length along the unit circle"""
    length = np.array([0.]*len(x))
    for i in range(1, len(x)):
        length[i] = length[i-1] + np.sqrt((x[i]-x[i-1])**2 + (y[i]-y[i-1])**2)
    return length


def fundamental_sin(n=100):
    """Define sine by height with respect to arc length"""
    x, y = circle_points(n)
    l = arc_length(x, y)
    return l, y


def fundamental_cos(n=100):
    """Define cosine by base leg length with respect to arc length"""
    x, y = circle_points(n)
    l = arc_length(x, y)
    return l, x


if __name__ == '__main__':
    x, y = fundamental_sin(1000)
    plt.plot(x, y)
    x2, y2 = fundamental_cos(1000)
    plt.plot(x, np.sin(x))
    plt.show()
