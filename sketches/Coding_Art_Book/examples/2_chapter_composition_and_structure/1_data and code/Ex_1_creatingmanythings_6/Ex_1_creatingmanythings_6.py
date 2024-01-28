""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## animating 4000 particles (with Particle class)

particle = [None] * 4000


def setup():
    py5.size(600, 600)
    py5.smooth()
    py5.no_stroke()

    ## loop through all 4000 particles and initialize
    for i in range(4000):
        particle[i] = Particle()


def draw():
    ## dark blue background
    py5.background(35, 27, 107)

    ## always draw from center of canvas
    py5.translate(py5.width / 2, py5.height / 2)

    ## loop through all particles
    for p in particle:
        ## change position and draw particle
        p.move()
        p.show()


## create a new class for our particle
class Particle:
    ## initialize
    def __init__(self):
        self.x = 0
        self.y = 0
        self.size = py5.random(0.5, 4)
        self.direction_x = py5.random(-1, 1)
        self.direction_y = py5.random(-1, 1)

    ## function to move the particle position in direction
    def move(self):
        self.x += self.direction_x
        self.y += self.direction_y

    ## draw the particle on the Processing canvas
    def show(self):
        py5.fill(238, 120, 138, self.size * 30)
        py5.ellipse(self.x, self.y, self.size, self.size)


py5.run_sketch()
