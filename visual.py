import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1340, 610
BALL_RADIUS = 20
BALL_COLOR = (0, 0, 255)
BACKGROUND_IMAGE = "court.png"  # Replace with your image file
SPEED = 5

# Coordinates
x = 100
y = HEIGHT // 2

# Direction
direction = 1  # 1 for right, -1 for left

# Create a window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ball Animation")

# Load the background image
background = pygame.image.load(BACKGROUND_IMAGE)
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Draw the background image
    screen.blit(background, (0, 0))

    # Update ball position
    x += direction * SPEED

    # Change direction when reaching edges
    if x < BALL_RADIUS or x > WIDTH - BALL_RADIUS:
        direction *= -1

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (x, y), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(30)
