""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## translated and scaled ellipses


def setup():
    ## setup canvas
    py5.size(400, 400)
    py5.background(208, 170, 208)
    py5.fill(113, 70, 132, 100)
    py5.stroke(246, 173, 113, 100)
    py5.stroke_weight(5)

    ## draw the first ellipse
    py5.ellipse(150, 150, 150, 150)

    ## second ellipse shifted to right and scaled down
    py5.translate(50, 50)
    py5.scale(0.9)
    py5.ellipse(150, 150, 150, 150)

    ## third ellipse shifted and scaled again
    py5.translate(50, 50)
    py5.scale(0.9)
    py5.ellipse(150, 150, 150, 150)

    ## fourth ellipse shifted and scaled again
    py5.translate(50, 50)
    py5.scale(0.9)
    py5.ellipse(150, 150, 150, 150)


py5.run_sketch()
