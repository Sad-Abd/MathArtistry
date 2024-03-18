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

    # Rectangle parameters
    rect_half_width = 100
    rect_half_height = 60

    # Compute SDF value for each line of the rectangle
    top_line_sdf_value = signed_distance_function_line(my, -rect_half_height)
    bottom_line_sdf_value = signed_distance_function_line(my, rect_half_height)
    left_line_sdf_value = signed_distance_function_line(mx, -rect_half_width)
    right_line_sdf_value = signed_distance_function_line(mx, rect_half_width)

    # Perform unions
    inter1_sdf_value = max(top_line_sdf_value, bottom_line_sdf_value)
    inter2_sdf_value = max(inter1_sdf_value, left_line_sdf_value)
    inter3_sdf_value = max(inter2_sdf_value, right_line_sdf_value)

    # Map SDF value to color
    inter_color = py5.remap(inter3_sdf_value, -rect_half_width, rect_half_width, 0, 255)

    # Draw rectangle
    py5.fill(255 - inter_color, inter_color, 0, 150)
    py5.rect(-rect_half_width, -rect_half_height, rect_half_width * 2, rect_half_height * 2)

    # Display SDF value
    py5.fill(0)
    py5.text_size(12)
    py5.text(f"Rectangle SDF: {inter3_sdf_value:.2f}", -py5.width / 2 + 10, py5.height / 2 - 20)
    py5.text(f"Top Line SDF: {top_line_sdf_value:.2f}", -py5.width / 2 + 10, py5.height / 2 - 40)
    py5.text(f"Bottom Line SDF: {bottom_line_sdf_value:.2f}", -py5.width / 2 + 10, py5.height / 2 - 60)
    py5.text(f"Left Line SDF: {left_line_sdf_value:.2f}", -py5.width / 2 + 10, py5.height / 2 - 80)
    py5.text(f"Right Line SDF: {right_line_sdf_value:.2f}", -py5.width / 2 + 10, py5.height / 2 - 100)

def signed_distance_function_line(p, q):
    return abs(p) - abs(q)

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
