import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up window
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space-Themed Bouncing Sphere")

# Set up the clock for FPS control
clock = pygame.time.Clock()

# Background color (dark space-like)
background_color = (10, 10, 25)

# Ball properties
ball_radius = 50
ball_color = (0, 255, 255)  # Neon cyan
ball_x, ball_y = screen_width // 2, screen_height // 2  # Start in the middle
ball_speed_x, ball_speed_y = 5, 4


# Create stars for the background
def draw_stars(surface, star_count=100):
    for _ in range(star_count):
        star_x = random.randint(0, screen_width)
        star_y = random.randint(0, screen_height)
        star_size = random.randint(1, 3)  # Star size will vary for depth
        pygame.draw.circle(surface, (255, 255, 255), (star_x, star_y), star_size)


# Draw the retro grid for the Tetris vibe
def draw_grid(surface):
    grid_color = (30, 30, 80)
    grid_size = 40
    for x in range(0, screen_width, grid_size):
        pygame.draw.line(surface, grid_color, (x, 0), (x, screen_height))
    for y in range(0, screen_height, grid_size):
        pygame.draw.line(surface, grid_color, (0, y), (screen_width, y))


# Draw the 2D glowing ball
def draw_glowing_ball(surface, center_x, center_y, radius, color):
    # Outer glow
    for i in range(10, 0, -1):
        glow_alpha = i * 12  # Alpha value for each glow layer
        glow_color = (color[0], color[1], color[2], glow_alpha)
        glow_surface = pygame.Surface((radius * 4, radius * 4), pygame.SRCALPHA)
        pygame.draw.circle(glow_surface, glow_color, (radius * 2, radius * 2), radius + (i * 5))
        surface.blit(glow_surface, (center_x - radius * 2, center_y - radius * 2), special_flags=pygame.BLEND_RGB_ADD)

    # Main ball with gradient (gives it a 3D look)
    for i in range(radius, 0, -1):
        shade_factor = i / radius
        shaded_color = (
            int(color[0] * shade_factor),
            int(color[1] * shade_factor),
            int(color[2] * shade_factor)
        )
        pygame.draw.circle(surface, shaded_color, (center_x, center_y), i)

    # Add a bright reflection to simulate light source
    pygame.draw.circle(surface, (255, 255, 255), (center_x - radius // 3, center_y - radius // 3), radius // 5)


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the ball
    ball_x += ball_speed_x
    ball_y += ball_speed_y

    # Bounce off the walls
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= screen_width:
        ball_speed_x = -ball_speed_x
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= screen_height:
        ball_speed_y = -ball_speed_y

    # Fill the screen with the background color
    screen.fill(background_color)

    # Draw the stars
    draw_stars(screen)

    # Draw the grid
    draw_grid(screen)

    # Draw the glowing ball
    draw_glowing_ball(screen, ball_x, ball_y, ball_radius, ball_color)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate at 60 FPS
    clock.tick(60)

