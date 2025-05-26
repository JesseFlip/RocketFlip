# Import the Pygame module
import pygame

# Import random
import random

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

# Define cnostants for screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
    
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
          self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
          self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
          self.rect.move_ip(-1, 0)
        if pressed_keys[K_RIGHT]:
          self.rect.move_ip(1, 0)

        # Keep player on the screen
        if self.rect.left < 0:
          self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
          self.rect.right = SCREEN_WIDTH
        if self.rect.top <=0:
          self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
          self.rect.bottom = SCREEN_HEIGHT
           
# Define Enemy object by extending pygame.sprit.Sprite
# The surface you draw on the screen is now an attribure of 'enemy'
class Enemy(pygame.sprite.Sprite):
   def __init__(self):
      super(Enemy, self).__init__()
      self.surf = pygame.Surface((20, 10))
      self.surf.fill((255, 255, 255))
      self.rect = self.surf.get_rect(
         center=(
            random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH = 100),
            random.randint(0, SCREEN_HEIGHT),
         )
      )
      self.speed = random.randint(5, 20)

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
   def update(self):
    self.rect.move_ip(-self.speed, 0)
    if self.rect.right < 0:
      self.kill()

# Create screen object
# The size is determined by the SCREEN_WIDTH & SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Instantiate the player
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for sollision detection and position updates
# - all_sprites is ussed for rendering
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# vVriable to keep the mainloop running
running = True

# Main loop
while running:
    # Check everything in the event queue 
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
           # Check if user hit escape key. If so, stop the game
            if event.key == K_ESCAPE:
                running = False
            # Else, check if user closed window, and stop app if so
        elif event.type == QUIT:
            running = False


    # Get key set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Fill the screen with black
    screen.fill((0, 0, 0))


    # Draw all sprites
    for entity in all_sprites:
      screen.blit(entity.surf, entity.rect)

    # Update the display
    pygame.display.flip()