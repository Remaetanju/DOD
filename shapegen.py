import json
import random

import matplotlib.pyplot as plt

from random import randrange

from matplotlib.patches import Rectangle
from matplotlib.patches import Rectangle

Colors = ['Red', 'Green', 'Blue']


class Generator:
    def __init__(self, x, y, shape_size):
        self.x_limit = x
        self.y_limit = y
        self.shape_size = shape_size

    def generate_circle(self):
        randrange(10)
        return {'radius': randrange(self.shape_size), 'center': (randrange(self.x_limit), randrange(self.y_limit)), 'color': random.choice(Colors)}

    def generate_square(self):
        randrange(10)
        return {'height': randrange(self.shape_size), 'width': randrange(self.shape_size),
                'center': (randrange(self.x_limit), randrange(self.y_limit)), 'color': random.choice(Colors)}


class Scribe:

    @staticmethod
    def export_shapes_to_file(shapes, filename):
        with open(filename, 'w') as file:
            file.write(json.dumps(shapes))

    @staticmethod
    def import_shapes_from_file(filename):
        with open(filename, 'w') as file:
            return json.loads(file.read())


class Picasso:
    def __init__(self, shapes):
        # define Matplotlib figure and axis
        self.fig, self.ax = plt.subplots()

        for shape in shapes:
            # create simple line plot
            # ax.plot([0, 10], [0, 10])

            if 'radius' in shape.keys():
                circle = plt.Circle(shape['center'], radius=shape['radius'], fc='y')
                fig = plt.gcf()
                ax = fig.gca()
                ax.add_patch(circle)
            # # add rectangle to plot
            # ax.add_patch(Rectangle((1, 1), 2, 6))
            # ax.add_patch(circle)

            # display plot

    def print_shapes(self):
        plt.show()
