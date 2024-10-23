import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up the window size and title
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Aesthetic Bouncing Sphere")

# Set up the clock for FPS control
clock = pygame.time.Clock()

# Define the ball's properties
ball_radius = 40
ball_color = (0, 122, 255)  # Base blue color
ball_x, ball_y = screen_width // 2, screen_height // 2  # Start in the middle
ball_speed_x, ball_speed_y = 4, 3  # Velocity in X and Y directions

# Gravity and friction
gravity = 0.1
friction = 0.98

# Draw a gradient circle
def draw_gradient_ball(surface, center_x, center_y, radius, color):
    for i in range(radius, 0, -1):
        shade_factor = 1 - (i / radius)
        new_color = (
            int(color[0] * (1 - shade_factor)),
            int(color[1] * (1 - shade_factor)),
            int(color[2] * (1 - shade_factor))
        )
        pygame.draw.circle(surface, new_color, (center_x, center_y), i)

# Function to draw a simple background gradient
def draw_background_gradient(surface, color1, color2):
    for i in range(screen_height):
        blend = i / screen_height
        color = (
            int(color1[0] * (1 - blend) + color2[0] * blend),
            int(color1[1] * (1 - blend) + color2[1] * blend),
            int(color1[2] * (1 - blend) + color2[2] * blend)
        )
        pygame.draw


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Gravity and friction
    gravity = 0.2
    friction = 0.99

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Apply gravity
    #ball_speed_y += gravity

    # Bounce off the walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_speed_x = -ball_speed_x * friction  # Reduce speed slightly after bounce

    # Bounce off the floor/ceiling
    if ball_y + ball_radius >= screen_height:
        ball_speed_y = -ball_speed_y * friction  # Reduce speed slightly after bounce
        ball_y = screen_height - ball_radius  # Avoid ball sinking into the floor

    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # Fill the screen with a color (RGB - white background)
    screen.fill((255, 255, 255))

    # Draw the ball
    pygame.draw.circle(screen, ball_color, (ball_x, ball_y), ball_radius)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

