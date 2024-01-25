""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## rectangle rotation 1


def setup():
    py5.size(200, 200)
    py5.background(0)
    py5.rect_mode(py5.CENTER)

    ## draw white 'canvas'
    py5.fill(255)
    py5.rect(py5.width / 2, py5.height / 2, 200, 200)

    ## draw black rectangle on canvas
    py5.fill(0)
    py5.rect(py5.width / 2, py5.height / 2, 40, 40)


py5.run_sketch()
