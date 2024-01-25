""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## positioning rectangles


def setup():
    ## draw next rectangle with (21, 22) as center
    py5.rect_mode(py5.CENTER)
    py5.fill(255, 0, 0)
    py5.rect(21, 22, 70, 30, 10)

    ## draw next rectangle with (21, 22) as top-left corner
    py5.rect_mode(py5.CORNER)
    py5.fill(0, 0, 255)
    py5.rect(21, 22, 70, 30, 10)


py5.run_sketch()
