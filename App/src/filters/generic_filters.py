import math
import logging
import time


def generic_algorithm(_shapes):
    """
    :param _shapes: list of shapes described by json

    :return: None
    """
    filter = Filter()

    logging.info(f'Created a list of simplified shape objects for treatment, nb of elems: {len(_shapes)}')

    # operate on the simplified shape list here (filter, etc)
    timer = time.perf_counter()
    circle_list = filter.filter_generic_circle(_shapes)
    quadrilatere_list = filter.filter_generic_quadrilatere(_shapes)
    mutate_list = filter.mutation_generic_circle(circle_list)
    square_circle = filter.emission_generic_quadrilatere(mutate_list)
    square_quadrilatere = filter.emission_generic_quadrilatere(quadrilatere_list)
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


    @staticmethod
    def filter_generic_circle(shapes):

        circles_list = []

        for shape in shapes:
            if shape.get('radius') is not None:
                circles_list.append(shape)

        return circles_list

    @staticmethod
    def filter_generic_quadrilatere(shapes):
        quadrilatere_list = []

        for shape in shapes:
            if shape.get('height') is not None:
                quadrilatere_list.append(shape)

        return quadrilatere_list

    @staticmethod
    def mutation_generic_circle(cercles):
        mutation_shape = []

        for cercle in cercles:
            origin = (cercle.get("origin")[0] - cercle.get("radius"), cercle.get("origin")[1] - cercle.get("radius"))

            new_shape = dict(height=cercle.get("radius")*2, width=cercle.get("radius")*2, origin=origin, color=cercle.get("color"))
            mutation_shape.append(new_shape)

        return mutation_shape

    @staticmethod
    def emission_generic_quadrilatere(shapes):
        min_left = math.inf
        max_right = - math.inf
        max_top = - math.inf
        min_bottom = math.inf

        for shape in shapes:
            if shape.get("origin")[0] < min_left:
                min_left = shape.get("origin")[0]

            if shape.get("origin")[0] + shape.get("width") > max_right:
                max_right = shape.get("origin")[0] + shape.get("width")

            if shape.get("origin")[1] < min_bottom:
                min_bottom = shape.get("origin")[1]

            if shape.get("origin")[1] + shape.get("height") > max_top:
                max_top = shape.get("origin")[1] + shape.get("height")

        result_execution_data = dict(point_1=(min_left, min_bottom), point_2=(max_right, max_top), execution_time=0)
        return result_execution_data
