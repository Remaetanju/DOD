from Scribe import Scribe, Generator


def generate_dummy_shapes_if_not_exist():
    gen = Generator(15, 15, 10)
    dummy_shapes = list()
    dummy_shapes.append(gen.generate_circle())
    dummy_shapes.append(gen.generate_square())

    Scribe.export_shapes_to_file(dummy_shapes, '../test.json')


# def typed_algorithm():
#     pass
#
#
# def generic_algorithm():
#     pass
