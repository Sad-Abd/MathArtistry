import py5


def setup():
    # Set the window size to 400x400 pixels
    py5.size(400, 400)


def draw():
    # Clear the screen with white color
    py5.background(255)

    # Translate the drawing origin to the center of the window
    py5.translate(py5.width / 2, py5.height / 2)

    # Define the rectangle corners
    x1 = -100
    y1 = -100
    x2 = 100
    y2 = 100

    # Draw a rectangle with the specified parameters
    py5.stroke(0)  # Set the stroke color to black
    py5.rect(x1, y1, x2 - x1, y2 - y1)

    # Get the mouse coordinates relative to the center of the window
    mx = py5.mouse_x - py5.width / 2
    my = py5.mouse_y - py5.height / 2

    # Calculate the distance between the mouse position and the rectangle
    distance = signed_distance_function(mx, my, x1, y1, x2, y2)

    # Map the distance to a color
    c = py5.remap(distance, -1, 1, 0, 255)

    # Display the distance value
    py5.fill(0, c, 255 - c)
    py5.text_size(16)
    py5.text(
        "Distance: {:.2f}".format(distance), -py5.width / 2 + 10, py5.height / 2 - 20
    )


def signed_distance_function(x, y, x1, y1, x2, y2):
    """
    Calculate the signed distance from a point (x, y) to a rectangle defined
    by its bottom-left (x1, y1) and top-right (x2, y2) coordinates.
    """

    # Calculate the perpendicular distances from the point to the edges of the rectangle
    dist1 = x1 - x
    dist2 = x - x2
    dist3 = y1 - y
    dist4 = y - y2

    # Return the max perpendicular distance
    return max(dist1, dist2, dist3, dist4)


py5.run_sketch()
