class Filter:
    @staticmethod
    def filter_generique_circle(shapes):

        circles_list = []

        for shape in shapes:
            if shape.get('radius') is not None:
                circles_list.append(shape)

        return circles_list

    @staticmethod
    def filter_generique_quadrilatere(shapes):
        quadrilatere_list = []

        for shape in shapes:
            if shape.get('height') is not None:
                quadrilatere_list.append(shape)

        return quadrilatere_list

    @staticmethod
    def mutation_generique_circle(cercles):
        mutation_shape = []

        for cercle in cercles:

            new_shape = dict(height=cercle.radius, width=cercle.radius, center=cercle.center, color=cercle.color)
            mutation_shape.append(new_shape)

        return mutation_shape

    @staticmethod
    def emission_generique_quadrilatere(shapes):
        res = 0

        for shape in shapes:
            res = res + shape.get('width')*shape.get('height')

        return res
