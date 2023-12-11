import py5

def setup():
    py5.size(400, 400)

def draw():
    py5.background(255)
    py5.translate(py5.width / 2, py5.height / 2)

    # Draw the circle
    py5.stroke(0)
    fill_circle(0, 0, 80)

    # Get the mouse coordinates relative to the center
    mx = py5.mouse_x - py5.width / 2
    my = py5.mouse_y - py5.height / 2

    # Compute the signed distance function value
    sdf_value = signed_distance_function(mx, my, 0, 0, 80)

    # Map the signed distance function value to a color
    c = py5.remap(sdf_value, -1, 1, 0, 255)

    # Display the signed distance function value
    py5.fill(0, c, 255 - c)
    py5.text_size(16)
    py5.text("SDF Value: {:.2f}".format(sdf_value), -py5.width / 2 + 10, py5.height / 2 - 20)


def fill_circle(x, y, r):
    num_points = 100
    py5.begin_shape()
    for i in range(num_points + 1):
        theta = py5.remap(i, 0, num_points, 0, py5.TWO_PI)
        px = x + r * py5.cos(theta)
        py = y + r * py5.sin(theta)
        py5.vertex(px, py)
    py5.end_shape(py5.CLOSE)


def signed_distance_function(x, y, center_x, center_y, radius):
    distance = py5.dist(x, y, center_x, center_y)
    return distance - radius

py5.run_sketch()

