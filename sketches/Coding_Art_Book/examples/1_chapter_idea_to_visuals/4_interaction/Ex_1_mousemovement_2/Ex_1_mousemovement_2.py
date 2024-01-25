""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## line movement with mouse


def setup():
    py5.size(400, 400)


def draw():
    ## white background, black line color
    py5.background(255)
    py5.stroke(0)

    ## if the mouse is pressed, then ...
    if py5.is_mouse_pressed:
        ## ... draw an interesting line
        py5.line(py5.mouse_x, 150, 150, py5.mouse_y)


py5.run_sketch()
