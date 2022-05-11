from SimplifiedShapes import SimplifiedShape
import math
import logging
import time

def simplified_algorithm(_shapes):
    """
    :param _shapes: list of shapes described by json

    :return: None
    """
    filter = Filter()
    simplified_shapes = []

    for shape in _shapes:
        new_shape = SimplifiedShape(origin=shape.get('origin'), color=shape.get('color'), width=shape.get('width'), height=shape.get('height'), radius=shape.get('radius'))
        simplified_shapes.append(new_shape)

    logging.info(f'Created a list of simplified shape objects for treatment, nb of elems: {len(simplified_shapes)}')

    for elem in simplified_shapes:
        logging.info(elem.__dict__)

    # operate on the simplified shape list here (filter, etc)
    timer = time.perf_counter()
    circle_list = filter.filter_simplified_circle(simplified_shapes)
    quadrilatere_list = filter.filter_simplified_quadrilatere(simplified_shapes)
    mutate_list = filter.mutation_simplified_circle(circle_list)
    res = filter.emission_simplified_quadrilatere(mutate_list+quadrilatere_list)
    final_timer = time.perf_counter() - timer

    res["execution_time"] = final_timer*1000
    """ output shapes are now op to be displayed """
    return res


class Filter:

    @staticmethod
    def filter_simplified_circle(shapes):
        circles_list = []

        for shape in shapes:
            if shape.radius is not None:
                circles_list.append(shape)

        return circles_list

    @staticmethod
    def filter_simplified_quadrilatere(shapes):
        quadrilatere_list = []

        for shape in shapes:
            if shape.height is not None:
                quadrilatere_list.append(shape)

        return quadrilatere_list

    @staticmethod
    def mutation_simplified_circle(circles):
        mutation_shape = []

        for circle in circles:
            origin = (circle.origin[0] - circle.radius, circle.origin[1] - circle.radius)
            new_simple_shape = SimplifiedShape(origin=origin, color=circle.color,
                                               width=circle.radius*2, height=circle.radius*2,
                                               radius=None)
            mutation_shape.append(new_simple_shape)

        return mutation_shape

    @staticmethod
    def emission_simplified_quadrilatere(shapes):
        min_left = math.inf
        max_right = - math.inf
        max_top = - math.inf
        min_bottom = math.inf

        print("min_left " + str(min_left))
        print("max_right " + str(max_right))
        print("max_top " + str(max_top))
        print("min_bottom " + str(min_bottom))

        for shape in shapes:

            if shape.origin[0] < min_left:
                min_left = shape.origin[0]

            if shape.origin[0] + shape.width > max_right:
                max_right = shape.origin[0] + shape.width

            if shape.origin[1] < min_bottom:
                min_bottom = shape.origin[1]

            if shape.origin[1] + shape.height > max_top:
                max_top = shape.origin[1] + shape.height

            print()
            print("min_left " + str(min_left))
            print("max_right " + str(max_right))
            print("max_top " + str(max_top))
            print("min_bottom " + str(min_bottom))
            print()

        print("TEST")
        print("width: " + str(max_right - min_left))
        print("height: " + str(max_top - min_bottom))
        result_execution_data = dict(point_1=(min_left, min_bottom), point_2=(max_right, max_top), execution_time=0)

        print("coucou")
        print(result_execution_data["point_1"])

        return result_execution_data
