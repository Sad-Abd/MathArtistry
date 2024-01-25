""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## simple triangle


def setup():
    py5.fill(140, 40, 160)

    ## draw triangle between position (21, 22),
    ## position (31, 32), and position (41, 22)
    py5.triangle(21, 22, 31, 32, 41, 22)


py5.run_sketch()
