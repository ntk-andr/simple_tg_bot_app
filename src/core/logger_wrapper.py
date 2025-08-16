import logging
import os.path
import sys

from settings import settings

DATE_FORMAT = settings.DATE_FORMAT
LOG_FORMAT = settings.LOG_FORMAT
LOG_LEVEL = settings.LOG_LEVEL


class LoggerWrapper:
    def __init__(self, name: str, level: int = logging.DEBUG, mode: str = 'a'):
        self.filename = None
        self.path = None
        name = name.lower()
        self.create_dir()
        self.logger = logging.getLogger(name=name)
        self.logger.setLevel(level=level)

        stream_handler = logging.StreamHandler(stream=sys.stdout)

        self.filename = f'{self.path}/{name}.log'
        file_handler = logging.FileHandler(filename=self.filename, mode=mode)
        formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
        file_handler.setFormatter(fmt=formatter)

        self.logger.addHandler(hdlr=stream_handler)
        self.logger.addHandler(hdlr=file_handler)
        self.logger.info(f'LoggerWrapper init {self.filename}')

    def create_dir(self):
        self.path = './logs'
        if not os.path.exists(path=self.path):
            os.makedirs(self.path)

    def set_file_handler(self, name: str, mode: str = 'w'):
        self.filename = f'{self.path}/{name}.log'
        file_handler = logging.FileHandler(filename=self.filename, mode=mode)
        formatter = logging.Formatter(fmt=LOG_FORMAT, datefmt=DATE_FORMAT)
        file_handler.setFormatter(fmt=formatter)
        return file_handler
