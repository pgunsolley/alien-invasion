import sys
import os
import pygame
from src.constants import *
from src.rocket import Rocket


def run_game():
    """Main entry"""
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    bg_image = pygame.image.load(BG_IMAGE)
    rocket = Rocket(screen)

    # Start the main loop.
    while True:
        # Watch for keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill the background color.
        screen.blit(bg_image, (0, 0))

        # Render the rocket.
        rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
