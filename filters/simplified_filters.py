from SimplifiedShapes import SimplifiedShape
import math
import logging


def simplified_algorithm(_shapes):
    """
    :param _shapes: list of shapes described by json

    :return: None
    """
    filter = Filter()
    simplified_shapes = []

    for shape in _shapes:
        new_shape = SimplifiedShape(center=shape.get('center'), color=shape.get('color'), width=shape.get('width'), height=shape.get('height'), radius=shape.get('radius'))
        simplified_shapes.append(new_shape)

    logging.info(f'Created a list of simplified shape objects for treatment, nb of elems: {len(simplified_shapes)}')

    for elem in simplified_shapes:
        logging.info(elem.__dict__)

    # operate on the simplified shape list here (filter, etc)
    circle_list = filter.filter_simplified_circle(simplified_shapes)
    quadrilatere_list = filter.filter_simplified_quadrilatere(simplified_shapes)
    mutate_list = filter.mutation_simplified_circle(circle_list)
    res = filter.emission_simplified_quadrilatere(mutate_list+quadrilatere_list)

    for l in quadrilatere_list:
        print(l.width)
        print(l.height)
        print()

    for l in mutate_list:
        print(l.width)
        print(l.height)
        print()

    print(res)

    # then we re-export the data to json state
    output_shapes = []

    for shape in simplified_shapes:
        output_shapes.append(shape.to_json())

    """ output shapes are now op to be displayed """
    return output_shapes


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
            new_simple_shape = SimplifiedShape(center=circle.center, color=circle.color,
                                               width=circle.radius, height=circle.radius,
                                               radius=None)
            mutation_shape.append(new_simple_shape)

        return mutation_shape

    @staticmethod
    def emission_simplified_quadrilatere(shapes):
        res = 0

        min_left = math.inf
        max_right = - math.inf
        max_top = - math.inf
        min_bottom = math.inf

        print("min_left " + str(min_left))
        print("max_right " + str(max_right))
        print("max_top " + str(max_top))
        print("min_bottom " + str(min_bottom))

        for shape in shapes:

            if shape.center[0] - shape.width < min_left:
                min_left = shape.center[0] - shape.width

            if shape.center[0] + shape.width > max_right:
                max_right = shape.center[0] + shape.width

            if shape.center[1] - shape.height < min_bottom:
                min_bottom = shape.center[1] - shape.height

            if shape.center[1] + shape.height > max_top:
                max_top = shape.center[1] + shape.height

            print()
            print("min_left " + str(min_left))
            print("max_right " + str(max_right))
            print("max_top " + str(max_top))
            print("min_bottom " + str(min_bottom))
            print()

        print("TEST")
        print("width: " + str(max_right - min_left))
        print("height: " + str(max_top - min_bottom))

        return 0
