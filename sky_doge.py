# Import the Pygame module
import pygame

# import pygame.locals for easier access to key coordinates
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Initialize Pygame
pygame.init()

# Define cnostants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Create screen object
# The size is determined by the SCREEN_WIDTH & SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# vVriable to keep the mainloop running
running = True

# Main loop
while running:
    # Check everything in the event queue 
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
           # Check if user hit escape key. if so, stop the game
            if event.key == K_ESCAPE:
                running = False
            # Else, check if user closed window, and stop app if so
        elif event.type == QUIT:
            running = False

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Create a surface and pass it a tuple of the length and width
    surf = pygame.Surface((50, 50))

    # Put the center of surf at the center of the screen

    surf_center = (
        (SCREEN_WIDTH-surf.get_width())/2,
        (SCREEN_HEIGHT-surf.get_height())/2
    )

    # Give the surface a color different from treh background
    surf.fill((0, 0, 0))
    rect = surf.get_rect()

    # draw surf onto teh screen, centered
    screen.blit(surf, surf_center)
    pygame.display.flip()