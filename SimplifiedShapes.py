import logging


class SimplifiedShape:
    center = tuple()
    color = str()
    radius = int()
    width = int()
    height = int()

    def __init__(self, center, color, width=None, height=None, radius=None):
        logging.info(f'{center} {color} {width} {height} {radius}')
        
        if not radius or not (height and width):
            self.center = center
            self.color = color
            self.width = width
            self.height = height
            self.radius = radius
        else:
            raise Exception('missing a value when constructing SimplifiedShape')

    def is_circle(self):
        return bool(self.radius)

    def to_json(self):
        return dict(center=self.center, color=self.color, width=self.width, height=self.height, radius=self.radius)
