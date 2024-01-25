""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## rectangle rotation 3


def setup():
    ## setup canvas
    py5.size(200, 200)
    py5.background(0)
    py5.rect_mode(py5.CENTER)

    ## draw white 'canvas'
    py5.fill(255)
    py5.rect(py5.width / 2, py5.height / 2, 200, 200)

    ## translate to center point
    py5.translate(py5.width / 2, py5.height / 2)

    ## rotate by 10 degrees
    py5.rotate(py5.radians(10))

    ## draw black rectangle using the new (0, 0)
    py5.fill(0)
    py5.rect(0, 0, 40, 40)


py5.run_sketch()
