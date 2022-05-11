<<<<<<< HEAD:App/src/filters/typed_filters.py
from App.src.shapes.SimplifiedShapes import SimplifiedShape
=======
from AbstractShapes import Circle, Quadrilatere
>>>>>>> 244547fad831d377a8d926742a102746f77f6663:filters/typed_filters.py
import math
import logging
import time

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
    res = filter.emission_typed_quadrilatere(mutate_list+quadrilatere_list)
    final_timer = time.perf_counter() - timer

    print("aaaaaaaaaaa")
    print(res)
    print("bbbbbbbbbbb")

    res["execution_time"] = final_timer*1000
    """ output shapes are now op to be displayed """
    return res


class Filter:


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
        print("min_left "+str(min_left))
        print("max_right "+str(max_right))
        print("max_top "+str(max_top))
        print("min_bottom "+str(min_bottom))

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
            id += 1


        print("TEST")
        print("width: " + str(max_right-min_left))
        print("height: " + str(max_top-min_bottom))
        result_execution_data = dict(point_1=(min_left, min_bottom), point_2=(max_right, max_top), execution_time=0)

        return result_execution_data