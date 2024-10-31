import math
import cairo
import random

#  canvas dimensions
WIDTH, HEIGHT = 600, 600
BALL_RADIUS = 200
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(2 / 255, 85 / 255, 38 / 255)
context.paint()

#   'dots'
for _ in range(700):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.uniform(1, 3)  # Random 'dot' size
    context.set_source_rgb(236 / 255, 253 / 255, 0 / 255)  # yellow
    context.arc(x, y, size, 0, 2 * math.pi)
    context.fill()


def draw_sphere(context, center_x, center_y, radius):
    # main circle for the ball
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.1, center_x, center_y,
                                    radius)
    gradient.add_color_stop_rgb(0, 0.3, 0.3, 0.3)
    gradient.add_color_stop_rgb(0.7, 0.09, 0.09, 0.09)
    context.set_source(gradient)
    context.fill()
    # white circle
    shading = cairo.RadialGradient(center_x + radius * 0.2, center_y - radius * 0.2, radius * 0.05,
                                   center_x + radius * 0.2, center_y - radius * 0.2, radius * 0.4
                                   )
    shading.add_color_stop_rgb(0, 1, 1, 1)  # White center
    shading.add_color_stop_rgb(1, 0.9, 0.9, 0.9)  # Slightly grey edge
    context.set_source(shading)  # Set color to white

    white_circle_x = center_x
    white_circle_y = center_y
    context.arc(white_circle_x, white_circle_y, radius * 0.4, 0, 2 * math.pi)
    context.fill()

    # shadow around the white circle
    shadow_gradient = cairo.RadialGradient(white_circle_x, white_circle_y, radius * 0.35,
                                           white_circle_x, white_circle_y, radius * 0.45)
    shadow_gradient.add_color_stop_rgba(0, 0, 0, 0, 0.2)
    shadow_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)
    context.set_source(shadow_gradient)
    context.arc(white_circle_x, white_circle_y, radius * 0.45, 0, 2 * math.pi)
    context.fill()

    #  "8" number
    context.set_source_rgb(0, 0, 0)  # Set color to black for the number
    context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    context.set_font_size(radius * 0.5)
    context.move_to(white_circle_x - 29, white_circle_y + 34)  # Adjust position of the "8"
    context.show_text("8")


def draw_shadow(context, center_x, center_y, radius):
    """Draws a soft shadow under the pool ball."""
    shadow_gradient = cairo.RadialGradient(
        center_x, center_y + radius, radius * 0.2,
        center_x, center_y + radius, radius * 1.2
    )
    shadow_gradient.add_color_stop_rgba(0, 0, 0, 0, 0.6)  # Dark center
    shadow_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)  # Transparent edge
    context.set_source(shadow_gradient)
    context.arc(center_x, center_y + radius * 0.6, radius, 0, 2 * math.pi)
    context.fill()


# the 3D pool ball on the canvas
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)
draw_shadow(context, WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

# Saving
surface.write_to_png("3d_pool_ball2.png")
print("3D pool ball image created!")

