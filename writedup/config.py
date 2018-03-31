import os
import pathlib
from configparser import ConfigParser

class Config:
    FILE_NAME = '.writedup'
    PATH = os.path.expanduser(os.path.join('~', FILE_NAME))

    def __init__(self):
        self.data = ConfigParser()
        if not os.path.exists(self.PATH):
            pathlib.Path(self.PATH).touch()
        self.data.read([self.PATH])

    def get_defaults(self):
        return self.data['DEFAULT']

    def _write(self):
        with open(self.PATH, 'w') as cfg:
            self.data.write(cfg)

    def write_defaults(self, **kwargs):
        for key, value in kwargs.items():
            self.data['DEFAULT'][key] = value
        self._write()
