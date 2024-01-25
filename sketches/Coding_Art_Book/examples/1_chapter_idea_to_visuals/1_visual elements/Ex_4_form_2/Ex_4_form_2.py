""" Coding Art Book
   Yu Zhang + Mathias Funk, 2020
   Translated to py5 by Sad-Abd"""

import py5

## textured spheres with translations


def setup():
    ## set canvas size and ask for 3D canvas
    py5.size(640, 640, py5.P3D)

    ## white background, no outline for shapes
    py5.background(255)
    py5.no_stroke()

    ## load the texture image
    ## from https://pixabay.com/photos/earth-blue-planet-globe-planet-11015/
    img = py5.load_image("earth.jpg")

    ## create a shape and set the image as texture
    ellipse = py5.create_shape(py5.SPHERE, 100)
    ellipse.set_texture(img)

    ## from the left to right, draw the first 3D ellipse
    py5.translate(py5.width / 5, py5.height / 5, -150)
    py5.shape(ellipse)
    ## from the left to right, draw the second 3D ellipse
    py5.translate(py5.width / 5, py5.height / 5, 150)
    py5.shape(ellipse)
    ## from the left to right, draw the third 3D ellipse
    py5.translate(py5.width / 5, py5.height / 5, 150)
    py5.shape(ellipse)


py5.run_sketch()
