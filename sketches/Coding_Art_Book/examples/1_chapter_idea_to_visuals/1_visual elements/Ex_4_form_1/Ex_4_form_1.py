""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## simple sphere with lighting


def setup():
    py5.size(640, 640, py5.P3D)
    py5.background(208, 170, 208)
    py5.no_stroke()
    py5.fill(113, 70, 132)

    ## use a directional light in 3D space:
    ## first three values give light position,
    ## the rest is about the direction of the light
    py5.directional_light(251, 232, 255, 1, 0, -1)

    ## move camera
    py5.translate(py5.width / 2, py5.height / 2, -30)

    ## draw sphere with 180 pixel diameter
    py5.sphere(180)


py5.run_sketch()
