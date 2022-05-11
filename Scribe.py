import json


class Scribe:
    @staticmethod
    def export_shapes_to_file(shapes, filename):
        with open(filename, 'w') as file:
            file.write(json.dumps(shapes))

    @staticmethod
    def import_shapes_from_file(filename):
        with open(filename, 'r') as file:
            return json.load(file)
