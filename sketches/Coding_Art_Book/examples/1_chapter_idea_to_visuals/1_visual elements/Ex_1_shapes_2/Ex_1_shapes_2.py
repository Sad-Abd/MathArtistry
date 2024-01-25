""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## ellipse on canvas


def setup():
    ## set the size of the canvas
    py5.size(600, 600)

    ## paint the background first
    py5.background(208, 170, 208)

    ## set line color and width and fill color
    py5.stroke(246, 173, 113)
    py5.stroke_weight(10)
    py5.fill(113, 70, 132)

    ## draw the ellipse in center of canvas
    py5.ellipse(py5.width / 2, py5.height / 2, 320, 320)


py5.run_sketch()
