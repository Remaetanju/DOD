class AbstractShape:
    center = tuple()
    color = str()

    def __init__(self, center, color):
        self.center = center
        self.color = color


class Circle(AbstractShape):
    radius = int()

    def __init__(self, width, height, center, color):
        super(Circle, self).__init__(center, color)
        self.width = width
        self.height = height


class Quadrilatere(AbstractShape):
    width = int()
    height = int()

    def __init__(self, width, height, center, color):
        super(Quadrilatere, self).__init__(center, color)
        self.width = width
        self.height = height
