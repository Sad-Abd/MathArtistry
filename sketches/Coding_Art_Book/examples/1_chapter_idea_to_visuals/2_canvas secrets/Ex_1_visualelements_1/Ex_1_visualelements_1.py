""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## scaling different rectangles


def setup():
    ## set canvas size and background color
    py5.size(1200, 200)
    py5.background(208, 170, 208)

    ## draw circle and rectangle in original scale
    py5.stroke(246, 173, 113)
    py5.stroke_weight(5)
    py5.fill(113, 70, 132)
    py5.ellipse(705, 145, 355, 355)
    py5.rect(530, 20, 355, 235, 130)

    ## draw first scaled rectangle
    py5.scale(1.3, 1.4)
    py5.fill(113, 70, 132, 150)
    py5.rect(530, 20, 355, 175, 230)

    ## draw second scaled rectangle
    py5.scale(0.6)
    py5.fill(113, 70, 132, 60)
    py5.stroke(246, 173, 113, 80)
    py5.rect(530, 20, 355, 175, 230)


py5.run_sketch()
