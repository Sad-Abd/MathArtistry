""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## animating 4000 particles in round shape with interaction

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
        ## change position with added parameter depending on
        ## the distance from the mouse to the horizontal center
        p.move(abs(py5.width / 2 - py5.mouse_x))
        ## draw particle
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
    ## move function with additional parameter 'radius'
    ## that replaces the number 250 below
    def move(self, radius):
        ## calculate the particle's distance from the center
        position = py5.Py5Vector(self.x, self.y)
        if position.dist(py5.Py5Vector(0, 0)) > radius:
            ## create new random target position
            target = py5.Py5Vector(py5.random(-250, 250), py5.random(-250, 250))
            ## calculate the direction vector between current and target position
            direction = target - position
            ## divide direction by 600 to make the steps small
            direction /= 600
            ## set the new direction for the particle
            self.direction_x = direction.x
            self.direction_y = direction.y

        ## this is as before
        self.x += self.direction_x
        self.y += self.direction_y

    ## draw the particle on the Processing canvas
    def show(self):
        py5.fill(238, 120, 138, self.size * 30)
        py5.ellipse(self.x, self.y, self.size, self.size)


py5.run_sketch()
