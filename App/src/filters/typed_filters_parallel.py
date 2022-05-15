import math
import logging

import threading
from threading import Lock

from App.src.shapes.AbstractShapes import Circle, Quadrilatere
from App.src.tools.tools import Runtime

circles = []
quadrilateres = []


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
    new_p1_x = is_inf(square_circle["point_1"][0],square_quadrilatere["point_1"][0])
    new_p1_y = is_inf(square_circle["point_1"][1],square_quadrilatere["point_1"][1])

    new_p2_x = is_sup(square_circle["point_2"][0],square_quadrilatere["point_2"][0])
    new_p2_y = is_sup(square_circle["point_2"][1],square_quadrilatere["point_2"][1])

    res = dict(point_1=(new_p1_x, new_p1_y), point_2=(new_p2_x, new_p2_y), execution_time=0)
    return res


def filter_typed(shapes):
    for shape in shapes:
        if isinstance(shape, Circle):
            circles.append(shape)
        else:
            quadrilateres.append(shape)


def mutation_typed_circle(cercles):
    mutation_shape = []

    for cercle in cercles:
        origin = (cercle.origin[0] - cercle.radius, cercle.origin[1] - cercle.radius)
        mutation_shape.append(Quadrilatere(cercle.radius*2, cercle.radius*2, origin, cercle.color))

    return mutation_shape


def emission_typed_quadrilatere(shapes):

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


def typed_algorithm_parallel(_shapes, thread_nb):
    typed_shapes = []

    for shape in _shapes:
        if shape.get("radius"):
            new_shape = Circle(radius=shape.get('radius'), origin=shape.get('origin'), color=shape.get('color'))
        else:
            new_shape = Quadrilatere(width=shape.get('width'), height=shape.get('height'),
                                     origin=shape.get('origin'), color=shape.get('color'))
    
        typed_shapes.append(new_shape)
    
    logging.info(f'Created a list of simplified shape typed for treatment, nb of elems: {len(typed_shapes)}')
    
    for elem in typed_shapes:
        logging.info(elem.__dict__)
    
    # operate on the simplified shape list here (filter, etc)

    runtime = Runtime()
    runtime.start_nanoseconds()

    simplified_threads = [threading.Thread(target=filter_typed, args=[typed_shapes]) for i in range(thread_nb)]

    for t in simplified_threads:
        t.start()
    for t in simplified_threads:
        t.join()

    filter_typed(typed_shapes)

    mutate_list = mutation_typed_circle(circles)

    square_circle = emission_typed_quadrilatere(mutate_list)
    square_quadrilatere = emission_typed_quadrilatere(quadrilateres)

    res = generate_final_square(square_circle, square_quadrilatere)

    res["execution_time"] = (runtime.stop_nanoseconds())
    """ output shapes are now op to be displayed """
    return res