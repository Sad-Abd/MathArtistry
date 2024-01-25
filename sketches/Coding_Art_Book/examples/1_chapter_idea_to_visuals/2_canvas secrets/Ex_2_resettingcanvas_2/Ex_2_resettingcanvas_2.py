""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## scaling and reset with push and pop

def setup():
    ## scale canvas once and draw rectangle
    py5.scale(0.8)
    py5.rect(0, 0, 20, 20)

    ## save point
    py5.push_matrix()
    ## vertical stretch
    py5.scale(0.6, 1.2)
    py5.ellipse(10, 10, 20, 20)
    ## restore canvas
    py5.pop_matrix()

    ## draw rectangle in normal scaling as above
    py5.rect(30, 0, 20, 20)

    ## save point
    py5.push_matrix()
    ## horizontal stretch
    py5.scale(1.2, 0.6)
    py5.ellipse(40, 10, 20, 20)
    ## restore canvas
    py5.pop_matrix()

py5.run_sketch()
