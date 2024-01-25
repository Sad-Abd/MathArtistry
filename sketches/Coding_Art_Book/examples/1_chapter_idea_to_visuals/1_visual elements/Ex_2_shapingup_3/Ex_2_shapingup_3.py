""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## simple rectangle with rounded corners


def setup():
    py5.fill(140, 180, 20)

    ## draw rectangle at position (21, 22) with
    ## size given by width 70 and height 30
    ## rounded corners with 10 pixel radius
    py5.rect(21, 22, 70, 30, 10)


py5.run_sketch()
