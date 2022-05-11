import logging


class SimplifiedShape:
    origin = tuple()
    color = str()
    radius = int()
    width = int()
    height = int()

    def __init__(self, origin, color, width=None, height=None, radius=None):
        logging.info(f'{origin} {color} {width} {height} {radius}')
        
        if not radius or not (height and width):
            self.origin = origin
            self.color = color
            self.width = width
            self.height = height
            self.radius = radius
        else:
            raise Exception('missing a value when constructing SimplifiedShape')

    def is_circle(self):
        return bool(self.radius)

    def to_json(self):
        return dict(origin=self.origin, color=self.color, width=self.width, height=self.height, radius=self.radius)
