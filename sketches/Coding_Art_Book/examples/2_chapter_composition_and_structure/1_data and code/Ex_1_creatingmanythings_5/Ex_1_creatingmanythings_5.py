""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## animating 4000 particles

particle = [None] * 4000
direction = [None] * 4000


def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.no_stroke()

    ## loop through all 4000 particles
    for i in range(4000):
        ## initialize particle at center position with a third component
        ## that we use for size and color of the particle
        particle[i] = py5.Py5Vector(0, 0, py5.random(0.5, 4))
        ## initialize random particle direction
        direction[i] = py5.Py5Vector(py5.random(-1, 1), py5.random(-1, 1), 0)


def draw():
    ## dark blue background
    py5.background(35, 27, 107)

    ## always draw from center of canvas
    py5.translate(py5.width / 2, py5.height / 2)

    ## loop through all particles
    for i, p in enumerate(particle):
        ## change position
        p += direction[i]
        ## adjust individual color
        py5.fill(238, 120, 138, p.z * 30)
        ## draw particle shape
        py5.ellipse(p.x, p.y, p.z, p.z)


py5.run_sketch()
