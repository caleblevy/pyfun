#!/usr/bin/env python

"""A simple program for singing praise to God! Requires Mac OS X.

DISCLAIMER: The contents of this program are intended to be ridiculous,
useless, and amusing. The praising of God for extended durations may induce
boredom, strange looks from friends, and a general wasting of time.

Caleb Levy, March 2015.
"""

import sys
import time
import os

say = lambda phrase: os.system('say '+phrase)  # Run phrase through OS X say


def sing_praise(repetitions=1000):
    """Sing praise to YHWH a specified number of times."""
    try:
        # First check sys.argv for amount of praise
        reps = int(sys.argv[-1])
    except ValueError:
        # In case when believer was too enthralled to specify, use default
        reps = repetitions
    # Begin the prayer
    say("Let us sing praise to God %s times in:" % str(reps))
    # Provide users time to reflect before the service begins
    say('3...')
    time.sleep(1)
    say('2...')
    time.sleep(1)
    say('1...')
    time.sleep(1)

    for i in range(1, reps+1):
        time.sleep(.01)
        if i == 1:
            say("1st Refrain:")
        elif i == 2:
            say("2nd Refrain:")
        elif i == 3:
            say("3rd Refrain:")
        else:
            say("%sth Refrain:" % str(i))
        say("Praise YOWWAY!")  # YHWH must be spelled phonetically for OS X say
        say("Praise be to God!")

    say("Amen.")  # Conclude the prayer


if __name__ == '__main__':
    sing_praise()
