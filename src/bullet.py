import pygame
from src.constants import *


class Bullet(pygame.sprite.Sprite):
    """
    A PyGame Sprite subclass that represents bullet projectiles.
    """

    def __init__(self, weapon, color=(247, 73, 73), dimensions=(3, 15), speed=3):
        """
        Initialize the bullet.
        """
        super(Bullet, self).__init__()

        # Store the screen.
        self.screen = weapon.screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect((0, 0), dimensions)

        # Align the center and top of the bullet rect with the weapon's  rect.
        self.rect.centerx = weapon.rect.centerx
        self.rect.top = weapon.rect.top

        # Store bullet's position as a decimal value.
        self.y = float(self.rect.y)

        # Set physical properties.
        self.color = color
        self.speed = speed

    def update(self):
        """
        Update the bullet state.
        """

        # Update the decimal position.
        self.y -= self.speed

        # Update the rect position using the floating point number in self.y.
        self.rect.y = self.y

    def draw(self):
        """
        Draw the bullet to the screen.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
