import math
import logging
import time

from DOD.App.src.shapes.AbstractShapes import Circle, Quadrilatere


def typed_algorithm(_shapes):
    """
    :param _shapes: list of shapes described by json

    :return: None
    """
    filter = Filter()
    typed_shapes = []

    for shape in _shapes:
        if shape.get("radius"):
            new_shape = Circle(radius=shape.get('radius'), origin=shape.get('origin'), color=shape.get('color'))
        else:
            new_shape = Quadrilatere(width=shape.get('width'), height=shape.get('height'), origin=shape.get('origin'), color=shape.get('color'))

        typed_shapes.append(new_shape)

    logging.info(f'Created a list of simplified shape typed for treatment, nb of elems: {len(typed_shapes)}')

    for elem in typed_shapes:
        logging.info(elem.__dict__)

    # operate on the simplified shape list here (filter, etc)
    timer = time.perf_counter()
    circle_list = filter.filter_typed_circle(typed_shapes)
    quadrilatere_list = filter.filter_typed_quadrilatere(typed_shapes)
    mutate_list = filter.mutation_typed_circle(circle_list)
    square_circle = filter.emission_typed_quadrilatere(mutate_list)
    square_quadrilatere = filter.emission_typed_quadrilatere(quadrilatere_list)
    res = filter.generate_final_square(square_circle, square_quadrilatere)

    final_timer = time.perf_counter() - timer

    res["execution_time"] = final_timer*1000
    """ output shapes are now op to be displayed """
    return res

def is_sup(val1, val2):
    if val1 > val2:
        return val1
    else:
        return val2

def is_inf(val1, val2):
    if val1 > val2:
        return val2
    else:
        return val1

class Filter:


    @staticmethod
    def generate_final_square(square_circle, square_quadrilatere):


        new_p1_x = is_inf(square_circle["point_1"][0],square_quadrilatere["point_1"][0])
        new_p1_y = is_inf(square_circle["point_1"][1],square_quadrilatere["point_1"][1])

        new_p2_x = is_sup(square_circle["point_2"][0],square_quadrilatere["point_2"][0])
        new_p2_y = is_sup(square_circle["point_2"][1],square_quadrilatere["point_2"][1])


        res = dict(point_1=(new_p1_x, new_p1_y), point_2=(new_p2_x, new_p2_y), execution_time=0)
        print("generate_final_square")
        print(res)
        return res

    def filter_typed_circle(self, shapes):
        circles_list = []

        for shape in shapes:
            if type(shape) == Circle:
                circles_list.append(shape)

        return circles_list


    def filter_typed_quadrilatere(self, shapes):
        quadrilatere_list = []

        for shape in shapes:
            if type(shape) == Quadrilatere:
                quadrilatere_list.append(shape)

        return quadrilatere_list


    def mutation_typed_circle(self, cercles):
        mutation_shape = []

        for cercle in cercles:
            origin = (cercle.origin[0] - cercle.radius, cercle.origin[1] - cercle.radius)
            mutation_shape.append(Quadrilatere(cercle.radius*2, cercle.radius*2, origin, cercle.color))

        return mutation_shape


    def emission_typed_quadrilatere(self, shapes):

        min_left = math.inf
        max_right = - math.inf
        max_top = - math.inf
        min_bottom = math.inf


        id = 0
        for shape in shapes:
            if shape.origin[0] < min_left:
                min_left = shape.origin[0]
            if shape.origin[0] + shape.width > max_right:
                max_right = shape.origin[0] + shape.width
            if shape.origin[1] < min_bottom:
                min_bottom = shape.origin[1]
            if shape.origin[1] + shape.height > max_top:
                max_top = shape.origin[1] + shape.height

            id += 1

        result_execution_data = dict(point_1=(min_left, min_bottom), point_2=(max_right, max_top), execution_time=0)
        return result_execution_data