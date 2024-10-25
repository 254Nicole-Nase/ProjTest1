import math
import random
import cairo

WIDTH, HEIGHT = 600, 600
SPHERE_RADIUS = 200
center_x = WIDTH // 2
center_y = HEIGHT // 2
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)


def draw_sphere(context, center_x, center_y, radius):
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    # Draw the Earth with an enhanced ocean gradient
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 0.1, 0.3, 0.9)  # Deep ocean blue
    gradient.add_color_stop_rgb(1, 0, 0.1, 0.5)  # Darker edges
    context.set_source(gradient)
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.fill()

    # Add a subtle atmospheric glow around the Earth
    atmosphere_gradient = cairo.RadialGradient( center_x,center_y, SPHERE_RADIUS * 0.9, center_x, center_y, SPHERE_RADIUS * 1.3)
    atmosphere_gradient.add_color_stop_rgba(0, 0.5, 0.7, 1, 0.3)  # Blueish glow
    atmosphere_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)  # Transparent edge
    context.set_source(atmosphere_gradient)
    context.arc(center_x, center_y, SPHERE_RADIUS * 1.3, 0, 2 * math.pi)
    context.fill()

    # Add highlights to give the Earth a 3D effect
    highlight_gradient = cairo.RadialGradient( center_x - 70, center_y - 70, SPHERE_RADIUS * 0.3, center_x - 70, center_y - 70, SPHERE_RADIUS * 0.6 )
    highlight_gradient.add_color_stop_rgba(0, 1, 1, 1, 0.4)  # Bright highlight
    highlight_gradient.add_color_stop_rgba(1, 1, 1, 1, 0)  # Fading out
    context.set_source(highlight_gradient)
    context.arc(center_x, center_y, SPHERE_RADIUS, 0, 2 * math.pi)
    context.fill()

# Fill the background with black for space and code for random stars
context.set_source_rgb(0, 0, 0)  # Black background for space
context.paint()
for _ in range(300):
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.uniform(1, 3)  # Random star size
    # Brighter, whiter stars for a crisp background
    context.set_source_rgb(1, 1, 1)  # White stars
    context.arc(x, y, size, 0, 2 * math.pi)
    context.fill()


draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)
draw_sphere(context, center_x, center_y, SPHERE_RADIUS)
surface.write_to_png("3d_sphere.png")

print("3D sphere image created!")
