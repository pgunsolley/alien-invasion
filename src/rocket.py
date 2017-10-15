import pygame
from src.constants import *


class Rocket:
    """Represents the player."""

    def __init__(self, screen):
        """Initialize the rocket instance."""
        self.screen = screen

        # Load the ship image and get its rect (pygame surface)
        self.image = pygame.image.load(ROCKET_IMAGE)

        # The rect (surface) for the image
        self.rect = self.image.get_rect()


        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
