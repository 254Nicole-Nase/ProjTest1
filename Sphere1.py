import math
import cairo

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
context = cairo.Context(surface)
context.set_source_rgb(1,1,1)
context.paint()

def draw_sphere(context, center_x, center_y, radius):
    # Drawing the main black sphere with gradient for 3D effect
    context.arc(center_x, center_y, radius, 0, 2 * math.pi)
    gradient = cairo.RadialGradient(center_x - radius * 0.5, center_y - radius * 0.5, radius * 0.2,
                                    center_x, center_y, radius)
    gradient.add_color_stop_rgb(0, 0.2, 0.2, 0.2)  # Lighter at top left
    gradient.add_color_stop_rgb(1, 0, 0, 0)        # Darker at bottom right
    context.set_source(gradient)
    context.fill()

    # Adding the white circle for the number
    context.set_source_rgb(1, 1, 1)  # White color
    white_circle_x = center_x + radius * 0.2
    white_circle_y = center_y - radius * 0.2
    context.arc(white_circle_x, white_circle_y, radius * 0.4, 0, 2 * math.pi)
    context.fill()

    # Adding the number 8
    context.set_source_rgb(0, 0, 0)  # Black color for the text
    context.select_font_face("Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
    context.set_font_size(100)
    # Adjusting position of number "8" to be centered inside the white circle
    context.move_to(white_circle_x - 30, white_circle_y + 35)
    context.show_text("8")


# Drawing the 8-ball
draw_sphere(context, WIDTH // 2, HEIGHT // 2, 200)

# Saving the image
surface.write_to_png("3d_pool_ball.png")
print("3D pool ball image created!")

