"""
This is the tutorial's function module, slightly modified.

This is more of a 'procedures' script >.<
"""

# Todo: Replace this with my own solution.

import sys
import pygame
from src.constants import *
from src.bullet import Bullet


# Event Handling functions.
# Todo: Refactor these into the Eventer class.

# Check the event types.
def check_events(rocket):
    """
    Respond to keypresses and mouse events.
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            _check_keydown_events(event, rocket)
        elif event.type == pygame.KEYUP:
            _check_keyup_events(event, rocket)


# Check keyup events.
def _check_keyup_events(event, rocket):
    """
    Check for keyup events and respoond.
    """
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False


# Check keydown events.
def _check_keydown_events(event, rocket):
    """
    Check for keydown events and respond.
    """
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_ESCAPE:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        rocket.fire_bullet()


# Rendering functions.
# Todo: Refactor these into the Game class.
# Instead of passing things to render, use a strategy pattern or something.
def update_screen(screen, bg_image, rocket, fleet):
    """
    Update images on the screen and flip to the new screen.
    """

    # Merge (blit) the background image Surface with the screen Surface.
    screen.blit(bg_image, (0, 0))

    # Render the rocket.
    rocket.draw()

    # Render the fleet.
    fleet.draw()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
