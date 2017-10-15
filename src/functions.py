"""
This is the tutorial's function module.

Todo: Replace this with a more object oriented solution.
"""
import sys
import pygame
from src.constants import *


# Event Handling functions.
# Todo: Refactor these into the Eventer class.
def check_events(rocket):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = True
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                rocket.moving_right = False
            elif event.key == pygame.K_LEFT:
                rocket.moving_left = False


# Rendering functions.
# Todo: Refactor these into the Game class.
def update_screen(screen, bg_image, rocket):
    """Update images on the screen and flip to the new screen."""
    # Fill the background color.
    screen.blit(bg_image, (0, 0))

    # Render the rocket.
    rocket.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()