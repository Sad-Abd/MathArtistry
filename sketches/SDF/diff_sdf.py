import py5


def setup():
    py5.size(400, 400)


def draw():
    py5.background(255)
    py5.translate(py5.width / 2, py5.height / 2)

    # Draw grid
    draw_grid(20)

    # Draw axes
    draw_axes()

    # Get mouse coordinates relative to the center
    mx = py5.mouse_x - py5.width / 2
    my = py5.mouse_y - py5.height / 2

    # Circle 1 parameters
    circle1_center_x = -50
    circle1_center_y = 0
    circle1_radius = 80

    # Circle 2 parameters
    circle2_center_x = 50
    circle2_center_y = 0
    circle2_radius = 60

    # Compute SDF values for each circle
    circle1_sdf_value = signed_distance_function_circle(
        mx, my, circle1_center_x, circle1_center_y, circle1_radius
    )
    circle2_sdf_value = signed_distance_function_circle(
        mx, my, circle2_center_x, circle2_center_y, circle2_radius
    )

    # Perform difference operation
    diff_sdf_value = max(circle1_sdf_value, -circle2_sdf_value)

    # Map SDF values to colors
    circle1_color = py5.remap(circle1_sdf_value, -1, 1, 0, 255)
    circle2_color = py5.remap(circle2_sdf_value, -1, 1, 0, 255)
    diff_color = py5.remap(diff_sdf_value, -1, 1, 0, 255)

    # Draw circles
    py5.stroke(0, diff_color, 255 - diff_color)
    py5.fill(circle1_color, 150)
    fill_circle(circle1_center_x, circle1_center_y, circle1_radius)

    py5.fill(circle2_color, 150)
    fill_circle(circle2_center_x, circle2_center_y, circle2_radius)

    # Display SDF values (optional)
    py5.fill(0)
    py5.text_size(12)
    py5.text(
        f"Circle 1 SDF: {circle1_sdf_value:.2f}",
        -py5.width / 2 + 10,
        py5.height / 2 - 60,
    )
    py5.text(
        f"Circle 2 SDF: {circle2_sdf_value:.2f}",
        -py5.width / 2 + 10,
        py5.height / 2 - 40,
    )
    py5.text(
        f"Difference SDF: {diff_sdf_value:.2f}", -py5.width / 2 + 10, py5.height / 2 - 20
    )


def fill_circle(x, y, r):
    py5.begin_shape()
    for i in range(101):
        theta = py5.remap(i, 0, 100, 0, py5.TWO_PI)
        px = x + r * py5.cos(theta)
        py = y + r * py5.sin(theta)
        py5.vertex(px, py)
    py5.end_shape(py5.CLOSE)


def signed_distance_function_circle(x, y, center_x, center_y, radius):
    distance = py5.dist(x, y, center_x, center_y)
    return distance - radius


def draw_grid(spacing):
    py5.stroke(200)
    py5.stroke_weight(1)
    for x in range(int(-py5.width / 2), int(py5.width / 2) + 1, spacing):
        py5.line(x, -py5.height / 2, x, py5.height / 2)
    for y in range(int(-py5.height / 2), int(py5.height / 2) + 1, spacing):
        py5.line(-py5.width / 2, y, py5.width / 2, y)


def draw_axes():
    py5.stroke(0)
    py5.stroke_weight(2)
    # X-axis
    py5.line(-py5.width / 2, 0, py5.width / 2, 0)
    # Y-axis
    py5.line(0, -py5.height / 2, 0, py5.height / 2)


py5.run_sketch()
