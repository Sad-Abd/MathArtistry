""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## two rectangles with bouncing motion


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.background(160)
    py5.translate(0, py5.height / 2)

    ## linear rectangle
    py5.rect(py5.frame_count, 20, 20, 20)

    ## bouncing rectangle
    py5.rect(py5.frame_count, -abs(py5.sin(py5.frame_count / 20.0)) * 60, 20, 20)


py5.run_sketch()
