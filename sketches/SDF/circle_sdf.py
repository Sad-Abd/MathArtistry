import py5


def setup():
    # Set the window size to 400x400 pixels
    py5.size(400, 400)


def draw():
    # Clear the screen with white color
    py5.background(255)

    # Translate the drawing origin to the center of the window
    py5.translate(py5.width / 2, py5.height / 2)

    # Draw a circle with center at (0, 0) and radius 80
    py5.stroke(0)  # Set the stroke color to black
    fill_circle(0, 0, 80)  # Draw the circle using the `fill_circle` function

    # Get the mouse coordinates relative to the center of the window
    mx = py5.mouse_x - py5.width / 2
    my = py5.mouse_y - py5.height / 2

    # Compute the signed distance function value for the mouse position
    sdf_value = signed_distance_function(mx, my, 0, 0, 80)

    # Map the signed distance function value to a color
    c = py5.remap(sdf_value, -1, 1, 0, 255)

    # Display the signed distance function value
    py5.fill(0, c, 255 - c)
    py5.text_size(16)
    py5.text(
        "SDF Value: {:.2f}".format(sdf_value), -py5.width / 2 + 10, py5.height / 2 - 20
    )


def fill_circle(x, y, r):
    # Create a circle with center at (x, y) and radius r
    num_points = 100  # Number of points used to draw the circle
    py5.begin_shape()

    # Generate a set of points evenly spaced around the circle
    for i in range(num_points + 1):
        # Calculate the angle for each point
        theta = py5.remap(i, 0, num_points, 0, py5.TWO_PI)

        # Calculate the corresponding x and y coordinates for the point
        px = x + r * py5.cos(theta)
        py = y + r * py5.sin(theta)

        # Add the point to the shape
        py5.vertex(px, py)

    py5.end_shape(py5.CLOSE)


def signed_distance_function(x, y, center_x, center_y, radius):
    """Calculate the signed distance function for a circle centered at (center_x, center_y) with radius 'radius'."""
    distance = py5.dist(x, y, center_x, center_y)
    return distance - radius


py5.run_sketch()
