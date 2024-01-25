""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## two rectangles with bouncing motion and color change


def setup():
    py5.size(400, 400)
    py5.rect_mode(py5.CENTER)


def draw():
    py5.background(160)
    py5.translate(0, py5.height / 2)

    ## change color according to frameCount
    py5.fill(py5.frame_count % (20 * py5.PI) * 10)

    ## bouncing rectangle (same as before)
    py5.rect(py5.frame_count, -abs(py5.sin(py5.frame_count / 20.0)) * 60, 20, 20)

    ## linear rectangle with snap-back motion
    py5.rect(py5.frame_count, 20, 20, 20)
    py5.translate(25, 15)
    py5.rotate(py5.radians(90 - (py5.frame_count % (20 * py5.PI))))


py5.run_sketch()
