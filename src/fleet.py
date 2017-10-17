from src.constants import *
from pygame.sprite import Group
from src.gamecore import Renderable


class Fleet(Renderable):
    """
    A fleet of a sprites.

    Pass a reference to a class object of the sprite.
    """
    def __init__(self, sprite_class, screen):
        super(Fleet, self).__init__()
        """
        Instantiate the Fleet.

        Pass a valid sprite class object (non-instance) and main screen object.

        :param sprite_class:
        :param screen:
        """
        # Instantiate the dimensions dictionary.
        self.dimensions = {}

        # Store the sprite class object (non-instance).
        self.sprite_class = sprite_class

        # Since we need to pass a reference to the main screen for each sprite in this game,
        # store a local reference to the screen object.
        self.screen = screen

        # Prepare a sprite group to hold the fleet.
        self.sprites = Group()

        # Direction 1 represents right; -1 represents left.
        self.direction = 1

    def create(self):
        """
        Create the fleet by copying the passed Sprite.
        """
        # Create an initial object in order to calculate available_space and number_of_sprites
        sprite = self.sprite_class(self.screen)

        # Calculate the dimensional limits for the fleet.
        # This is used by the loop.
        self.dimensions = self._calculate_dimensions_from_sprite(sprite)

        for row_number in range(self.dimensions['number_of_rows']):
            for sprite_number in range(self.dimensions['number_of_sprites']):
                sprite = self.sprite_class(self.screen)
                self._modify_sprite_coordinates(sprite, self.dimensions['sprite_width'], sprite_number, row_number)
                self.sprites.add(sprite)

    @staticmethod
    def _modify_sprite_coordinates(sprite, sprite_width, sprite_number, row_number):
        """
        Modify the sprite coordinates to fit the fleet.
        """
        sprite.x = sprite_width + 2 * sprite_width * sprite_number
        sprite.rect.x = sprite.x
        sprite.rect.y = sprite.rect.height + 2 * sprite.rect.height * row_number

    @staticmethod
    def _calculate_dimensions_from_sprite(sprite):
        """
        Calculate the dimensions of the fleet based on a passed sprite object.

        :param sprite:
        :return: tuple
        """
        sprite_width = sprite.rect.width
        sprite_height = sprite.rect.height
        available_space_x = SCREEN_WIDTH - 2 * sprite_width
        available_space_y = SCREEN_HEIGHT - 3 * sprite_height - sprite_height * 2
        return {
            'sprite_width': sprite_width,
            'sprite_height': sprite_height,
            'available_space_x': available_space_x,
            'available_space_y': available_space_y,
            'number_of_sprites': int(available_space_x / (2 * sprite_width)),
            'number_of_rows': int(available_space_y / (2 * sprite_height))
        }

    def draw(self):
        """
        Call the draw method on the self.sprites Group

        :return:
        """
        self.sprites.draw(self.screen)
