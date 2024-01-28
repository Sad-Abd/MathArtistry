""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## random dots 1


def setup():
    py5.size(400, 400)
    py5.background(35, 27, 107)
    py5.no_stroke()


def draw():
    py5.fill(238, 120, 138, 250)
    py5.ellipse(py5.random(0, py5.width), py5.random(0, py5.height), 15, 15)

    py5.apply_filter(py5.BLUR, 1)


py5.run_sketch()
