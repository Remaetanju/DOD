from AbstractShapes import Circle, Quadrilatere
from SimplifiedShapes import SimplifiedShape
import math


class Filter:


    def filter_object_circle(self, shapes):
        circles_list = []

        for shape in shapes:
            if type(shape) == Circle:
                circles_list.append(shape)

        return circles_list


    def filter_object_quadrilatere(self, shapes):
        quadrilatere_list = []

        for shape in shapes:
            if type(shape) == Quadrilatere:
                quadrilatere_list.append(shape)

        return quadrilatere_list


    def mutation_object_circle(self, cercles):
        mutation_shape = []

        for cercle in cercles:
            mutation_shape.append(Quadrilatere(cercle.height, cercle.width, cercle.center, cercle.color))

        return mutation_shape


    def emission_object_quadrilatere(self, shapes):
        res = 0

        left = shapes[0].center[0]
        right = shapes[0].center[1]
        top = shapes[0].height
        bottom = 0

        left_id = 0
        right_id = 0
        top_id = 0
        bottom_id = 0

        id = 0

        for shape in shapes:

            if shape.center[0] < left:
                left = shape.center[0]
                left_id = id

            elif shape.center[0] > right:
                right = shape.center[0]
                right_id = id

            if shape.center[1] < bottom:
                bottom = shape.center[1]
                bottom_id = id

            elif shape.center[1] > top:
                top = shape.center[1]
                top_id = id

            id +1


        print("TEST")
        print(left)
        print(right)
        print(top)
        print(bottom)

        return  0








    def filter_generique_circle(self, shapes):

        circles_list = []

        for shape in shapes:
            if shape.get('radius') != None:
                circles_list.append(shape)

        return circles_list


    def filter_generique_quadrilatere(self, shapes):
        quadrilatere_list = []

        for shape in shapes:
            if shape.get('height') != None:
                quadrilatere_list.append(shape)

        return quadrilatere_list


    def mutation_generique_circle(self, cercles):
        mutation_shape = []

        for cercle in cercles:
            mutation_shape.append({'height': cercle.radius, 'width': cercle.radius,
                'center': cercle.center, 'color': cercle.color})

        return mutation_shape


    def emission_generique_quadrilatere(self, shapes):
        res = 0

        for shape in shapes:
            res = res + shape.get('width')*shape.get('height')

        return res






    def filter_simplified_circle(self, shapes):
        circles_list = []

        for shape in shapes:
            if shape.radius != None:
                circles_list.append(shape)

        return circles_list


    def filter_simplified_quadrilatere(self, shapes):
        quadrilatere_list = []

        for shape in shapes:
            if shape.height != None:
                quadrilatere_list.append(shape)

        return quadrilatere_list


    def mutation_simplified_circle(self, cercles):
        mutation_shape = []

        for cercle in cercles:
            mutation_shape.append(SimplifiedShape(center=cercle.center , color=cercle.color , width=cercle.radius, height=cercle.radius, radius=None))

        return mutation_shape


    def emission_simplified_quadrilatere(self, shapes):
        res = 0

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

            if shape.center[0]- shape.width < min_left:
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
            id += 1


        print("TEST")
        print("width: " + str(max_right-min_left))
        print("height: " + str(max_top-min_bottom))

        return  0