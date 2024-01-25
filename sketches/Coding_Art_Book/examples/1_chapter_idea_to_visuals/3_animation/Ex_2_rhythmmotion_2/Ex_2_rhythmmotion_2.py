""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## shifting movement (with sine)


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.background(160)
    py5.translate(py5.width / 2, py5.height / 2)
    py5.rect(py5.sin(py5.frame_count / 20.0) * py5.width / 2, 20, 20, 20)


py5.run_sketch()
