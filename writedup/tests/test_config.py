import os
import unittest

from writedup.config import Config

class TestConfig(unittest.TestCase):
    def test_creation(self):
        try:
            os.remove(Config.PATH)
        except FileNotFoundError:
            pass
        config = Config()
        self.assertTrue(os.path.exists(Config.PATH))

    def test_write_defaults(self):
        config = Config()
        defaults = {
            'roll_no': '1614023',
            'batch': 'A2',
        }
        config.write_defaults(**defaults)
        read_defaults = config.get_defaults()
