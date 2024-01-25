""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## scaling and reset


def setup():
    ## scale canvas once and draw rectangle
    py5.scale(0.8)
    py5.rect(0, 0, 20, 20)

    ## reset canvas
    py5.reset_matrix()

    ## next scale, draw rectangle
    py5.scale(0.6)
    py5.rect(0, 0, 20, 20)


py5.run_sketch()
