""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## simple movement


def setup():
    py5.size(400, 400)


def draw():
    py5.background(160)
    py5.rect(py5.frame_count, 30, 10, 10)


py5.run_sketch()
