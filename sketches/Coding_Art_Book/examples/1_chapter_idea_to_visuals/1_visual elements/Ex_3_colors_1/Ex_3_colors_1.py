""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## colors and bars (made for big screen size)


def setup():
    py5.size(1920, 1080)
    py5.background(255)
    ## set 30 pixel line weight
    py5.stroke_weight(30)

    ## set color and draw line
    py5.stroke(9, 37, 87)
    py5.line(0, 980, py5.width, 980)

    py5.stroke(135, 3, 17)
    py5.line(0, 10, py5.width, 10)

    py5.stroke(9, 37, 87)
    py5.line(0, 90, py5.width, 90)

    py5.stroke(211, 179, 15)
    py5.line(100, 0, 100, py5.height)

    py5.stroke(211, 179, 15)
    py5.line(0, 650, py5.width, 650)

    ## many more lines ...


py5.run_sketch()
