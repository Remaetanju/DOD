from shapegen import Generator
from shapegen import Scribe


if __name__ == '__main__':
    gen = Generator(15, 15, 10)
    shapes = list()

    shapes.append(gen.generate_circle())
    shapes.append(gen.generate_square())

    Scribe.export_shapes_to_file(shapes, 'test.json')

