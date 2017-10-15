import unittest
import pygame
from src.eventer import Eventer


class TestEventer(unittest.TestCase):
    """Test the Eventer object."""
    def setUp(self):
        self.eventer = Eventer()
        self.eventer.register_emitter(pygame.event)
        self.eventer.on('')

    def test_register_event_emitter(self):
        pass


if __name__ == '__main__':
    unittest.main()
