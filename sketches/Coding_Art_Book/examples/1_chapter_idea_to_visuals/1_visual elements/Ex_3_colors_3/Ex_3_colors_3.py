""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## colors and bars (made for big screen size)


def setup():
    py5.size(1920, 1080)
    py5.background(255)
    ## set 30 pixel py5.lineweight
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

    py5.stroke(135, 3, 17)
    py5.line(0, 700, py5.width, 700)
    py5.stroke(9, 37, 87)
    py5.line(0, 350, py5.width, 350)
    py5.stroke(135, 3, 17)
    py5.line(1850, 0, 1850, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(240, 0, 240, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(0, 50, py5.width, 50)
    py5.stroke(135, 3, 17)
    py5.line(650, 0, 650, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(780, 0, 780, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(0, 200, py5.width, 200)
    py5.stroke(211, 179, 15)
    py5.line(1780, 0, 1780, py5.height)
    py5.stroke(9, 37, 87)
    py5.line(170, 0, 170, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(0, 400, py5.width, 400)
    py5.stroke(211, 179, 15)
    py5.line(1920, 0, 1920, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(1600, 0, 1600, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(1500, 0, 1500, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(1300, 0, 1300, py5.height)
    py5.stroke(211, 179, 15)
    py5.line(0, 850, py5.width, 850)
    py5.stroke(211, 179, 15)
    py5.line(0, 900, py5.width, 900)
    py5.stroke(211, 179, 15)
    py5.line(0, 1050, py5.width, 1050)


py5.run_sketch()
