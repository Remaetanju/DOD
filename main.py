import logging
from tk import App


def logging_config():

    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    logging.basicConfig(filename=None, level=logging.DEBUG)
    # logging.info(f'available loggers: {loggers}')


if __name__ == '__main__':
    logging_config()
    app = App(500, 500)
    app.run()
