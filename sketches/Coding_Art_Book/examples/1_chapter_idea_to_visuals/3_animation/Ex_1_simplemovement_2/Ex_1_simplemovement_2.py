""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## simple movement with rotation


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.background(160)
    py5.translate(py5.frame_count, 30)
    py5.rotate(py5.radians(py5.frame_count * (360 / (20 * py5.PI))))
    py5.rect(0, 0, 20, 20)


py5.run_sketch()
