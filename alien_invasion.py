import sys
import os
import pygame
from src.constants import *
from src.rocket import Rocket
from src.alien import Alien
from src.functions import *
from pygame.sprite import Group


def run_game():
    """Main entry"""
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    bg_image = pygame.image.load(BG_IMAGE)

    # Todo: Remove the dependency to pass the screen into an object, like Rocket.
    # Move this to the Game object/Eventer object.
    rocket = Rocket(screen)

    # Create an alien.
    alien = Alien(screen)

    # Start the main loop.
    # Todo: Refactor this into the Game class and Eventer class (event loop).
    while True:
        # Check event loop
        # Todo: Make it so that you don't need to pass the rocket. Figure this out in the Game class.
        check_events(rocket)

        # Update objects that are on the screen
        rocket.update()

        # Re render the screen and everything registered on the screen.
        update_screen(screen, bg_image, rocket, alien)


run_game()
