import logging
from tkinter import *
from App.src.tk_ui import ShapeApp


def logging_config():

    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]

    logging.basicConfig(filename=None, level=logging.DEBUG, format='%(levelname)s | %(name)s | %(message)s | %(thread)d')
    # logging.info(f'available loggers: {loggers}')


if __name__ == '__main__':
    logging_config()
    app = ShapeApp(500, 500)
    app.run()
