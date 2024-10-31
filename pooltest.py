import math
import cairo

# Constants
WIDTH, HEIGHT = 600, 600
BALL_RADIUS = 200

# Create surface and context
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)

def draw_sphere(context, center_x, center_y, radius):
    """Draws the black 8-ball with a gradient for the 3D effect."""
    # 3D gradient for the ball
    gradient = cairo.RadialGradient(
        center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
        center_x, center_y, radius
    )
    gradient.add_color_stop_rgb(0, 0.2, 0.2, 0.2)  # Lighter at the top left
    gradient.add_color_stop_rgb(1, 0, 0, 0)        # Darker at the bottom

    # Draw the black sphere
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    context.set_source(gradient)
    context.fill()

    # Add a glossy highlight
    context.set_source_rgba(1, 1, 1, 0.5)  # Semi-transparent white
    context.arc(center_x - radius * 0.4, center_y - radius * 0.4, radius * 0.15, 0, 2 * math.pi)
    context.fill()

    # Draw the white number circle with shading
    shading = cairo.RadialGradient(
        center_x + radius * 0.2, center_y - radius * 0.2, radius * 0.05,
        center_x + radius * 0.2, center_y - radius * 0.2, radius * 0.4
    )
    shading.add_color_stop_rgb(0, 1, 1, 1)  # White center
    shading.add_color_stop_rgb(1, 0.9, 0.9, 0.9)  # Slightly grey edge

    context.set_source(shading)
    white_circle_x = center_x + radius * 0.2
    white_circle_y = center_y - radius * 0.2
    context.arc(white_circle_x, white_circle_y, radius * 0.4, 0, 2 * math.pi)
    context.fill()

    # Add the number 8 with centered text
    context.set_source_rgb(0, 0, 0)  # Black text color
    context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    context.set_font_size(100)

    # Use text extents to center the number perfectly
    text = "8"
    (x_bearing, y_bearing, text_width, text_height, _, _) = context.text_extents(text)
    text_x = white_circle_x - text_width / 2
    text_y = white_circle_y + text_height / 2

    context.move_to(text_x, text_y)
    context.show_text(text)

def draw_shadow(context, center_x, center_y, radius):
    """Draws a soft shadow under the pool ball."""
    shadow_gradient = cairo.RadialGradient(
        center_x, center_y + radius, radius * 0.2,
        center_x, center_y + radius, radius * 1.2
    )
    shadow_gradient.add_color_stop_rgba(0, 0, 0, 0, 0.6)  # Dark center
    shadow_gradient.add_color_stop_rgba(1, 0, 0, 0, 0)    # Transparent edge

    context.set_source(shadow_gradient)
    context.arc(center_x, center_y + radius * 0.6, radius, 0, 2 * math.pi)
    context.fill()

def draw_glow_background(context):
    """Creates a glowing, sleek background."""
    # Radial gradient for glowing background
    gradient = cairo.RadialGradient(
        WIDTH // 2, HEIGHT // 2, 100,  # Light center
        WIDTH // 2, HEIGHT // 2, 300   # Fade out to edges
    )
    gradient.add_color_stop_rgb(0, 0.1, 0.1, 0.2)  # Cool blue at the center
    gradient.add_color_stop_rgb(1, 0, 0, 0.1)      # Dark at the edges

    context.set_source(gradient)
    context.rectangle(0, 0, WIDTH, HEIGHT)
    context.fill()

# Draw shadow and 8-ball
draw_glow_background(context)
draw_shadow(context, WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
draw_sphere(context, WIDTH // 2, HEIGHT // 2, BALL_RADIUS)

# Save the image
surface.write_to_png("enhanced_3d_pool_ball.png")
print("Enhanced 3D pool ball image created!")





