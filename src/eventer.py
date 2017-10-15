import pygame

class Eventer:
    """
    Manager events within the event loop.

    Event Handlers must be passed functions.

    self.events:    Holds the current events
    self.observers: Holds registered observer functions.
    self.emitters:  Holds objects that emit events.

    author: Patrick Gunsolley
    """
    def __init__(self):
        """Initialize the Eventer instance."""
        self.events = []
        self.handlers = {}
        self.emitters = []

    def register_emitter(self, emitter):
        """
        Register an event emitter.

        This will allow for custom event emitters.

        :param emitter:
        :return:
        """
        self.emitters = emitter

    def update_events(self):
        """Check the events."""
        for emitter in self.emitters:
            self.events = emitter.get()

    def on(self, event, handler):
        """
        Register a handler function.

        Todo: Find a way to check if an event is a valid event name.
        """

        self.handlers[event] = handler

    def check_observers(self):
        """Check the observers against the registered events."""
        for event, handler in self.handlers.items():
            if event in self.events:
                handler()
