import pygame

class Eventer:
    """
    Manager events within the event loop.

    Observers must be passed functions.

    self.events:    Holds the current events
    self.observers: Holds registered observer functions.
    self.emitters:  Holds objects that emit events.

    author: Patrick Gunsolley
    """
    def __init__(self):
        """Initialize the Eventer instance."""
        self.events = []
        self.observers = {}
        self.emitters = []

    def register_event_emitter(self, emitter):
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

    def on(self, event, observer):
        """
        Register an observer function.

        Todo: Find a way to check if an event is a valid event name.
        """

        self.observers[event] = observer

    def check_observers(self):
        """Check the observers against the registered events."""
        for event, observer in self.observers.items():
            if event in self.events:
                observer()
