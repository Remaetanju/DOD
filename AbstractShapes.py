import random

class AbstractShape:
    center = tuple()
    color = str()

    def __init__(self, origin, color):
        self.origin = origin
        self.color = color


class Circle(AbstractShape):
    radius = int()

    def __init__(self, radius, origin, color):
        super(Circle, self).__init__(origin, color)
        self.radius = radius


class Quadrilatere(AbstractShape):
    width = int()
    height = int()

    def __init__(self, width, height, origin, color):
        super(Quadrilatere, self).__init__(origin, color)
        self.width = width
        self.height = height