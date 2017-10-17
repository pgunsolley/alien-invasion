import sys
import os
import pygame
from src.constants import *
from src.rocket import Rocket
from src.alien import Alien
from src.fleet import Fleet
from src.functions import *
from src.gamecore import Game
from src.observer import *


def run_game_new():
    """
    The new way to run the game using GameCore framework, by me :)

    :return:
    """
    game = Game()
    game.set_background_image(BG_IMAGE)
    game.set_player(Rocket)

    game.add_observer(pygame.KEYDOWN, pygame.K_RIGHT, player_move_right)
    game.add_observer(pygame.KEYDOWN, pygame.K_LEFT, player_move_left)
    game.add_observer(pygame.KEYUP, pygame.K_RIGHT, player_stop_moving_right)
    game.add_observer(pygame.KEYUP, pygame.K_LEFT, player_stop_moving_left)


def run_game():
    """
    Main
    """
    # Initialize game and create a screen object.
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption(CAPTION)
    bg_image = pygame.image.load(BG_IMAGE)

    # Move this to the Game object/Eventer object.
    # Todo: Use the Player class instead.
    rocket = Rocket(screen)

    # Create an alien fleet.
    aliens = Fleet(Alien, screen)
    aliens.create()

    # Start the main loop.
    # Todo: Refactor this into the Game class and Eventer class (event loop).
    while True:
        # Check event loop
        # Todo: Make it so that you don't need to pass the rocket. Figure this out in the Game class.
        check_events(rocket)

        # Update the player's state.
        rocket.update()

        # Re render the screen and everything registered on the screen.
        # This calls the blitme/draw methods.
        # Todo: Refactor this inside the event loop inside Game object.
        update_screen(screen, bg_image, rocket, aliens)


run_game()
