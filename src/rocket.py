import pygame
from src.constants import *
from pygame.sprite import Group
from src.bullet import Bullet


class Rocket:
    """Represents the player."""

    def __init__(self, screen):
        """Initialize the rocket instance."""

        # Store a reference to the screen object (main Surface)
        self.screen = screen

        # Load the ship image.
        # This will return a surface
        self.image = pygame.image.load(ROCKET_IMAGE)

        # Get the Rect object of the self.image surface.
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Ship center.
        #
        # Pygame Note:
        #
        # We are using floating points for setting position in order
        # to achieve a finer level of control when doing calculations, however
        # rects (surfaces) only work with integers.
        # Convert the integer value of self.rect.centerx to a float and store.
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

        # Ship settings
        # Todo: Import this from a separate settings abstraction.
        self.speed = 1.5

        # Setup a bullet bag.
        # Todo: Maybe abstract this into the game Class later.
        self.bullets = Group()
        self.bullet_limit = 3

    def update(self):
        """Update the ship's state."""

        # Update the floating point value of the center position.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed

        # Update rect object from self.center.
        self.rect.centerx = self.center

        # Update any bullets bullets.
        self._update_bullets()

    def _update_bullets(self):
        """Update the bullets."""
        if len(self.bullets) > 0:
            for bullet in self.bullets.sprites():
                bullet.update()
        self._delete_offscreen_bullets()

    def _delete_offscreen_bullets(self):
        """Remove bullets that are not on screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        self._blit_bullets()

    def _blit_bullets(self):
        """Draw the bullet surfaces."""
        # Todo: Refactor this later... remove the bullet update?
        if len(self.bullets) > 0:
            for bullet in self.bullets.sprites():
                bullet.draw()

    def fire_bullet(self):
        """Fire a bullet."""
        if len(self.bullets) < self.bullet_limit:
            self.bullets.add(Bullet(self))
