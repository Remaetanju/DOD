from shapegen import Generator
from shapegen import Scribe
from shapegen import Picasso
from SimplifiedShapes import SimplifiedShape
from Filter import Filter

import logging


def generate_dummy_shapes_if_not_exist():
    gen = Generator(15, 15, 10)
    dummy_shapes = list()
    dummy_shapes.append(gen.generate_circle())
    dummy_shapes.append(gen.generate_square())

    Scribe.export_shapes_to_file(dummy_shapes, 'test.json')


def simplified_algorithm(_shapes):
    """
    :param _shapes: list of shapes described by json

    :return: None
    """
    filter = Filter()
    simplified_shapes = []

    for shape in _shapes:
        new_shape = SimplifiedShape(center=shape.get('center'), color=shape.get('color'), width=shape.get('width'), height=shape.get('height'), radius=shape.get('radius'))
        simplified_shapes.append(new_shape)

    logging.info(f'Created a list of simplified shape objects for treatment, nb of elems: {len(simplified_shapes)}')

    for elem in simplified_shapes:
        logging.info(elem.__dict__)

    # operate on the simplified shape list here (filter, etc)
    circle_list = filter.filter_simplified_circle(simplified_shapes)
    quadrilatere_list = filter.filter_simplified_quadrilatere(simplified_shapes)
    mutate_list = filter.mutation_simplified_circle(circle_list)
    res = filter.emission_simplified_quadrilatere(mutate_list+quadrilatere_list)


    for l in quadrilatere_list:
        print(l.width)
        print(l.height)
        print()

    for l in mutate_list:
        print(l.width)
        print(l.height)
        print()

    print(res)

    # then we re-export the data to json state
    output_shapes = []

    for shape in simplified_shapes:
        output_shapes.append(shape.to_json())

    """ output shapes are now op to be displayed """
    return output_shapes


def typed_algorithm():
    pass


def generic_algorithm():
    pass


def logging_config():

    loggers = [logging.getLogger(name) for name in logging.root.manager.loggerDict]
    logging.basicConfig(filename=None, level=logging.DEBUG)
    # logging.info(f'available loggers: {loggers}')


if __name__ == '__main__':
    logging_config()
    generate_dummy_shapes_if_not_exist()

    shapes = Scribe.import_shapes_from_file('test.json')
    simplified_algorithm(_shapes=shapes)
    # typed_algorithm()
    # generic_algorithm()
