from shapegen import Generator
from shapegen import Scribe
from shapegen import Picasso
from SimplifiedShapes import SimplifiedShape
import logging


def generate_dummy_shapes_if_not_exist():
    gen = Generator(15, 15, 10)
    dummy_shapes = list()
    dummy_shapes.append(gen.generate_circle())
    dummy_shapes.append(gen.generate_square())

    Scribe.export_shapes_to_file(dummy_shapes, 'test.json')


def simplified_algorithm(_shapes):
    simplified_shapes = []

    for shape in _shapes:
        new_shape = SimplifiedShape(center=shape.get('center'), color=shape.get('color'), width=shape.get('width'), height=shape.get('height'), radius=shape.get('radius'))
        simplified_shapes.append(new_shape)

    logging.info(f'Created a list of simplified shape objects for treatment, nb of elems: {len(simplified_shapes)}')


def typed_algorithm():
    pass


def generic_algorithm():
    pass


def logging_config():

    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    logging.basicConfig(filename=None, level=logging.DEBUG)
    logging.info(f'available loggers: {loggers}')


if __name__ == '__main__':
    logging_config()
    generate_dummy_shapes_if_not_exist()

    shapes = Scribe.import_shapes_from_file('test.json')
    simplified_algorithm(_shapes=shapes)
    # typed_algorithm()
    # generic_algorithm()
