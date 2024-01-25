""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## mouse movement


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.background(160)

    ## the first rectangle is static
    py5.rect(50, 75, 50, 50)

    ## the second rectangle is dynamic
    py5.rect(py5.mouse_x, py5.mouse_y, 50, 50)


py5.run_sketch()
