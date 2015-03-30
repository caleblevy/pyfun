#!/usr/bin/env python

"""Writes a python file that, when executed, will produce a stack overflow
without employing recursion.

Also note that despite some seriously screwey indentation, this program is
pep8.

Caleb Levy, Spring 2014.
"""


def deep_call(n=2048):
    program_start = """a = 2


def double0(x):
    return x + x

"""

    def_list = []
    for i in range(n):
        def_string = """
def double%s(x):
    return double%s(x)

""" % (str(i+1), str(i))
        def_list.append(def_string)

    prog = [program_start] + def_list + [
        """
b = double%s(a)
""" % str(i+1)
        ]
    prog_text = ''.join(prog)
    with open('rec.py', 'w') as f:
        f.write(prog_text)

if __name__ == '__main__':
    deep_call()
