import sys
import os
import pygame
from src.constants import *
from src.rocket import Rocket
from src.functions import *


def run_game():
    """Main entry"""
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    bg_image = pygame.image.load(BG_IMAGE)
    rocket = Rocket(screen)

    # Start the main loop.
    # Todo: Refactor this into the Game class and Eventer class (event loop).
    while True:
        # Check event loop
        check_events(rocket)

        # Update objects that are on the screen
        rocket.update()

        # Re render the screen and everything registered on the screen.
        update_screen(screen, bg_image, rocket)


run_game()
