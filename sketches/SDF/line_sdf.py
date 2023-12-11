import py5
import numpy as np

# Define the starting point and end point of the line
p1, p2 = (0, 0), (np.random.rand() * py5.width, np.random.rand() * py5.height)


def setup():
    # Set the window size to 400x400 pixels
    py5.size(400, 400)


def draw():
    # Clear the screen with white color
    py5.background(255)

    # Translate the drawing origin to the center of the window
    py5.translate(py5.width / 2, py5.height / 2)

    # Set the stroke weight to make the line thicker
    py5.stroke_weight(4)  # You can adjust the thickness by changing the argument

    # Draw a line representing the SDF
    py5.stroke(0)  # Set the stroke color to black
    draw_line(p1, p2)  # Draw the line using the `draw_line` function

    # Draw red "s" at the start point
    py5.fill(255, 0, 0)
    py5.text("s", *p1)

    # Draw red "e" at the end point
    py5.text("e", *p2)

    # Get the mouse coordinates relative to the center of the window
    mx = py5.mouse_x - py5.width / 2
    my = py5.mouse_y - py5.height / 2

    # Compute the signed distance function value for the mouse position using dLine
    sdf_value = dLine(np.array([[mx, my]]), *p1, *p2)

    # Map the signed distance function value to a color
    c = py5.remap(sdf_value, -1, 1, 0, 255)

    # Display the signed distance function value
    py5.fill(0, c, 255 - c)
    py5.text_size(16)
    py5.text(
        "SDF Value: {:.2f}".format(sdf_value), -py5.width / 2 + 10, py5.height / 2 - 20
    )


def draw_line(p1, p2):
    # Create a line with the given points
    py5.begin_shape()
    py5.vertex(*p1)  # Start point
    py5.vertex(*p2)  # End point
    py5.end_shape()


def dLine(P, x1, y1, x2, y2):
    """
    Calculate the signed distance from point P to a line segment defined
    by two endpoints (x1, y1) and (x2, y2).
    """
    a = np.array([x2 - x1, y2 - y1])
    a = a / np.linalg.norm(a)
    b = P - np.array([x1, y1])
    d = np.dot(b, np.array([a[1], -a[0]]))
    return d[0]


py5.run_sketch()
