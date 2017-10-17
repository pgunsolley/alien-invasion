import pygame
from src.constants import *
from src.player import Player
from src.rocket import Rocket
import abc


class _MainLoop:
    """
    The main event/game loop.

    Only instantiate inside of a gamecore.Game instance.

    :return:
    """
    def __init__(self):
        """
        Initialize the MainLoop
        """
        # The player object.
        self._player = None

        # The running flag.
        self._running = False

        # Queue of Renderable objects.
        self._renderables = []

        # Event manager.
        self.event_manager = _EventManager()

    def set_player(self, player):
        """
        Set the player.

        The game should instantiate the Player instance and pass it as arg.

        :param player:
        :return:
        """
        self._player = player

    def stop(self):
        """
        Stop the loop.
        (stops the game)

        :return:
        """
        self._running = False

    def start(self):
        """
        Run the loop.

        :return:
        """
        if not self._running:
            self._running = True
            while self._running:
                self.event_manager.call(self._player)
                self.
                pass

    def add_renderable(self, renderable):
        """
        Add an instantiated Renderable to the renderables list.

        :return:
        """
        self._renderables.append(renderable)


class Game:
    """
    The main class for the GameCore framework.
    """
    def __init__(self, screen_size=(1280, 900)):
        """
        Instantiate everything the game needs.
        """
        # Screen.
        # This will be referenced to by every Sprite in the game.
        self._screen = pygame.display.set_mode(screen_size)

        # Game loop
        self._loop = _MainLoop()

        # Declare a player member
        self._player_set = False

        self._background_image_set = False

    def set_background_image(self, bg_image):
        """
        Blit a background image to the screen.

        :param bg_image:
        :return:
        """
        if not self._background_image_set:
            self._background_image_set = True
            self._screen.blit(bg_image, (0, 0))

    def set_player(self, sprite):
        """
        Set a player object.

        :return:
        """
        if self._player_set is False:
            self._loop.set_player(Player(sprite(self._screen)))
            return
        print("Player is already set; co-op is not yet supported.")

    @staticmethod
    def set_caption(caption):
        """
        Set the game caption.

        :param caption:
        :return:
        """
        pygame.display.set_caption(caption)

    def add_observer(self, event_type, key, handler, **kwargs):
        """
        Set an event handler for a pygame event type.

        Use pygame constants for the event_type.

        ex: game.on(pygame.QUIT, exit_game)

        :param event_type:
        :param handler:
        :param key:
        :return self:
        """
        self._loop.event_manager.connect(event_type, key, handler, **kwargs)
        return self

    def render(self, renderable):
        """
        Add a new sprite or custom object to the game.

        :param renderable:
        :return:
        """

        # TODO: Add a ABC for renderable objects.
        self._loop.add_renderable(renderable(self._screen))

    def start(self):
        """
        Start the game loop.

        Make sure all configurations and observers are set before calling this :)

        :return:
        """
        self._loop.start()

    def stop(self):
        """
        Stop the game loop.
        :return:
        """
        self._loop.stop()


class _EventManager:
    """
    The manager of events and stuffs.
    """
    def __init__(self):
        """
        Initialize Eventer.
        """
        # Event handlers should be registered as event[type][key] = handler_func
        # Ship with pygame.quit :)
        self._event_handlers = {
            pygame.KEYDOWN: {
                pygame.K_ESCAPE: pygame.quit
            }
        }

    def connect(self, event_type, key, handler, **kwargs):
        """
        Connect a handler callable to a pygame event.
        :param event_type:
        :param key:
        :param handler:
        :return:
        """
        if event_type in pygame and type(event_type) == int:
            self._event_handlers[event_type][key] = handler

    def call(self, player):
        """
        Call event handlers for all pygame events.

        Event handlers will always be passed an event and the player object.

        :return:
        """
        for event in pygame.event.get():
            if event in self._event_handlers:
                self._event_handlers[event.type][event.key](event=event, player=player)


class Renderable(abc.ABC):
    """
    Represents a custom sprite-like object that can be blit to the pygame screen.
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass