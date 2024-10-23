import cairo
import math
import random

# Constants for the image size
WIDTH, HEIGHT = 800, 800
SPHERE_RADIUS = 200
SPHERE_CENTER_X = WIDTH // 2
SPHERE_CENTER_Y = HEIGHT // 2

# Create an image surface
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

# Fill the background with black for space
context.set_source_rgb(0, 0, 0)  # Black background
context.paint()

# Draw a starry background
for _ in range(300):  # Increased number of stars for a richer background
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    size = random.uniform(1, 3)  # Random star size
    context.set_source_rgb(1, 1, 1)  # White stars
    context.arc(x, y, size, 0, 2 * math.pi)
    context.fill()

# Draw the Earth with an enhanced ocean gradient
ocean_gradient = cairo.RadialGradient(
    SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS * 0.5,
    SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS
)
ocean_gradient.add_color_stop_rgb(0, 0.1, 0.3, 0.9)  # Deep ocean blue
ocean_gradient.add_color_stop_rgb(1, 0, 0.1, 0.5)    # Darker edges

context.set_source(ocean_gradient)
context.arc(SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS, 0, 2 * math.pi)
context.fill()

# Add a subtle atmospheric glow around the Earth
atmosphere_gradient = cairo.RadialGradient(
    SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS * 0.9,
    SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS * 1.3
)
atmosphere_gradient.add_color_stop_rgba(0, 0.5, 0.7, 1, 0.3)  # Blueish glow
atmosphere_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)         # Transparent edge

context.set_source(atmosphere_gradient)
context.arc(SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS * 1.3, 0, 2 * math.pi)
context.fill()

# Add highlights to give the Earth a 3D effect
highlight_gradient = cairo.RadialGradient(
    SPHERE_CENTER_X - 70, SPHERE_CENTER_Y - 70, SPHERE_RADIUS * 0.3,
    SPHERE_CENTER_X - 70, SPHERE_CENTER_Y - 70, SPHERE_RADIUS * 0.6
)
highlight_gradient.add_color_stop_rgba(0, 1, 1, 1, 0.4)  # Bright highlight
highlight_gradient.add_color_stop_rgba(1, 1, 1, 1, 0)    # Fading out

context.set_source(highlight_gradient)
context.arc(SPHERE_CENTER_X, SPHERE_CENTER_Y, SPHERE_RADIUS, 0, 2 * math.pi)
context.fill()

# Save the result to a PNG file
surface.write_to_png("space_earth.png")
