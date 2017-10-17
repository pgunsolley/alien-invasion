import pygame
from src.constants import *


class Alien(pygame.sprite.Sprite):
    """
    Represents an alien.
    """
    def __init__(self, screen):
        """
        Initialize Alien.
        """
        super(Alien, self).__init__()

        # Alien speed.
        self.speed = 1

        # Store the screen
        self.screen = screen

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load("./resources/images/alien.bmp")

        # Build and return a rect object from the image (Surface) object.
        self.rect = self.image.get_rect()

        # Start each new alien at the top left of the screen.
        # Do this by setting the (x, y) coordinates to the width and height.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def update(self):
        """
        Update the alien state.

        :return:
        """
        self.x += self.speed
        self.rect.x = self.x

    def blitme(self):
        """
        Draw the alien at its current location.
        """
        self.screen.blit(self.image, self.rect)
