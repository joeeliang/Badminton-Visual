import pygame
import sys
import json

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1340, 610
BALL_RADIUS = 20
BALL_COLOR = (0, 0, 255)
BACKGROUND_IMAGE = "court.png"  # Replace with your image file
SPEED = 15

# Load the JSON data from a file
with open("shotdata.json", "r") as json_file:
    data = json.load(json_file)

# Extract the start and end coordinates from the JSON data
rally = data["rallies"][0]  # Assuming you want coordinates from the first rally
coordinates = [shot["endCoord"] for shot in rally["shots"]]
# Add serve coords
coordinates.insert(0, rally["shots"][0]["startCoord"])
current_target_index = 0
x, y = coordinates[current_target_index]

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

    # Calculate the direction towards the current target
    endCoordx, endCoordy = coordinates[current_target_index]
    dx = endCoordx - x
    dy = endCoordy - y
    distance = ((dx ** 2) + (dy ** 2)) ** 0.5

    # Normalize the direction and update the ball's position
    if distance > 0:
        x += (dx / distance) * SPEED
        y += (dy / distance) * SPEED

    # Check if the ball has reached the current target
    if distance < SPEED:
        current_target_index += 1
        if current_target_index >= len(coordinates):
            pygame.quit()
            sys.exit()

    # Draw the ball
    pygame.draw.circle(screen, BALL_COLOR, (int(x), int(y)), BALL_RADIUS)

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.delay(30)