import pygame
import abc


class Game:
    """
    The main class for the GameCore framework.
    """
    def __init__(self, screen_size=(1280, 900)):
        """
        Instantiate everything the game needs.
        """
        # The player object.
        self._player = None

        # The running flag.
        self._running = False

        # Queue of Renderable objects.
        self._renderables = []

        # Event manager.
        self._event_manager = _EventManager()

        # Screen.
        # This will be referenced to by every Sprite in the game.
        self._screen = pygame.display.set_mode(screen_size)

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
        if self._player is None:
            self.set_player(Player(sprite(self._screen)))
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
        self._event_manager.connect(event_type, key, handler, **kwargs)
        return self

    def render(self, renderable):
        """
        Add a new sprite or custom object to the game.

        :param renderable:
        :return:
        """

        self.add_renderable(renderable(self._screen))

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
                self._event_manager.call(self._player)
                # Todo: Call draw on all renderables.
                pass

    def add_renderable(self, renderable):
        """
        Add an instantiated Renderable to the renderables list.

        :return:
        """
        if renderable == Renderable:
            self._renderables.append(renderable)
            return
        raise TypeError("Argument must be an instance of gamecore.Renderable.")


class _EventManager:
    """
    The manager of events and stuffs.
    """
    def __init__(self):
        """
        Initialize gamecore._EventManager.
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
    Abstract Renderable
    Represents a custom sprite-like object that can be blit to the pygame screen.
    """
    def __init__(self):
        pass

    @abc.abstractmethod
    def draw(self):
        """
        Called by event loop to draw the object to the screen.

        :return:
        """
        pass


class Player(Renderable):
    """
    Represents the player.

    This object is a container that wraps a sprite.

    Pass an instantiated sprite object on initialization.
    """
    def __init__(self, sprite):
        super(Player, self).__init__()
        """
        Pass in a sprite instance.

        :param sprite:
        """
        self.sprite = sprite
        # Set up the player position.

    def update(self):
        """
        Update the self.sprite state.

        :return:
        """
        pass

    def draw(self):
        """
        Call blitme on the sprite.

        :return:
        """
        pass