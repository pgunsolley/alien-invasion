import sys
import pygame
from src import constants

def run_game():
    """Main entry"""

    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    bg_image = pygame.image.load(constants.BG_IMAGE)

    # Start the main loop.
    while True:
        # Watch for keyboard events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Fill the background color.
        screen.fill(bg_color)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


run_game()
