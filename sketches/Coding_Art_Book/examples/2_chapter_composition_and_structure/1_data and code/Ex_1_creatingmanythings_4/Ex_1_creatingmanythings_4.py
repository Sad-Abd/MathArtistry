""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## drawing a trace of dots with mouse

ellipses = [None] * 60


def setup():
    py5.size(400, 400)
    py5.background(35, 27, 107)
    py5.no_stroke()

    ## initialize the array
    for i in range(len(ellipses)):
        ellipses[i] = py5.Py5Vector(dim=2)


def draw():
    py5.apply_filter(py5.BLUR, 1)

    ## pick one position from the array
    p = ellipses[py5.frame_count % len(ellipses)]

    ## set mouse position if mouse is pressed
    if py5.is_mouse_pressed:
        p.x, p.y = py5.mouse_x, py5.mouse_y

    ## draw the position
    py5.fill(238, 120, 138, 250)
    py5.ellipse(p.x, p.y, 15, 15)


py5.run_sketch()
