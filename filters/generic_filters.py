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
    res = filter.emission_generic_quadrilatere(mutate_list+quadrilatere_list)
    final_timer = time.perf_counter() - timer

    res["execution_time"] = final_timer*1000
    """ output shapes are now op to be displayed """
    return res


class Filter:
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
        print("min_left " + str(min_left))
        print("max_right " + str(max_right))
        print("max_top " + str(max_top))
        print("min_bottom " + str(min_bottom))

        for shape in shapes:


            if shape.get("origin")[0] < min_left:
                min_left = shape.get("origin")[0]

            if shape.get("origin")[0] + shape.get("width") > max_right:
                max_right = shape.get("origin")[0] + shape.get("width")

            if shape.get("origin")[1] < min_bottom:
                min_bottom = shape.get("origin")[1]

            if shape.get("origin")[1] + shape.get("height") > max_top:
                max_top = shape.get("origin")[1] + shape.get("height")

            print("AZERTY")
            print("min_left " + str(shape.get("width")))
            print("max_right " + str(shape.get("height")))
           # print("max_top " + str(max_top))
            #print("min_bottom " + str(min_bottom))
            print()

        print("TEST")
        print("width: " + str(max_right - min_left))
        print("height: " + str(max_top - min_bottom))
        result_execution_data = dict(point_1=(min_left, min_bottom), point_2=(max_right, max_top), execution_time=0)

        print("coucou")
        print(result_execution_data["point_1"])

        return result_execution_data
