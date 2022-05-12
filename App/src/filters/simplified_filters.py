import math
import logging
import time

from App.src.shapes.SimplifiedShapes import SimplifiedShape


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


def generate_final_square(square_circle, square_quadrilatere):
    new_p1_x = is_inf(square_circle["point_1"][0], square_quadrilatere["point_1"][0])
    new_p1_y = is_inf(square_circle["point_1"][1], square_quadrilatere["point_1"][1])

    new_p2_x = is_sup(square_circle["point_2"][0], square_quadrilatere["point_2"][0])
    new_p2_y = is_sup(square_circle["point_2"][1], square_quadrilatere["point_2"][1])

    res = dict(point_1=(new_p1_x, new_p1_y), point_2=(new_p2_x, new_p2_y), execution_time=float())
    return res


def filter_simplified_circle(shapes):
    circles_list = list()
    for shape in shapes:
        if shape.radius is not None:
            circles_list.append(shape)
    return circles_list


def filter_simplified_quadrilatere(shapes):
    quadrilatere_list = list()
    for shape in shapes:
        if shape.height is not None:
            quadrilatere_list.append(shape)
    return quadrilatere_list


def mutation_simplified_circle(circles):
    mutation_shape = list()
    for circle in circles:
        origin = (circle.origin[0] - circle.radius, circle.origin[1] - circle.radius)
        new_simple_shape = SimplifiedShape(origin=origin, color=circle.color, width=circle.radius * 2,
                                           height=circle.radius * 2, radius=None)
        mutation_shape.append(new_simple_shape)
    return mutation_shape


def emission_simplified_quadrilatere(shapes):
    min_left = math.inf
    max_right = - math.inf
    max_top = - math.inf
    min_bottom = math.inf

    for shape in shapes:
        if shape.origin[0] < min_left:
            min_left = shape.origin[0]

        if shape.origin[0] + shape.width > max_right:
            max_right = shape.origin[0] + shape.width

        if shape.origin[1] < min_bottom:
            min_bottom = shape.origin[1]

        if shape.origin[1] + shape.height > max_top:
            max_top = shape.origin[1] + shape.height

    result_execution_data = dict(point_1=(min_left, min_bottom), point_2=(max_right, max_top), execution_time=float())
    return result_execution_data


def simplified_algorithm(_shapes):
    simplified_shapes = []

    for shape in _shapes:
        new_shape = SimplifiedShape(origin=shape.get('origin'), color=shape.get('color'), width=shape.get('width'),
                                    height=shape.get('height'), radius=shape.get('radius'))
        simplified_shapes.append(new_shape)
    logging.info(f'Created a list of simplified shape objects for treatment, nb of elems: {len(simplified_shapes)}')

    # operate on the simplified shape list here (filter, etc)
    start_time = time.time()

    circle_list = filter_simplified_circle(simplified_shapes)
    quadrilatere_list = filter_simplified_quadrilatere(simplified_shapes)
    mutate_list = mutation_simplified_circle(circle_list)

    square_circle = emission_simplified_quadrilatere(mutate_list)
    square_quadrilatere = emission_simplified_quadrilatere(quadrilatere_list)
    res = generate_final_square(square_circle, square_quadrilatere)

    final_timer = (time.time() - start_time)
    res["execution_time"] = final_timer * 1000
    return res
