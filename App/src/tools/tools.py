import json
from time import time_ns
from typing import Any


class Scribe:
    @staticmethod
    def export_shapes_to_file(shapes, filename):
        with open(filename, 'w') as file:
            file.write(json.dumps(shapes))

    @staticmethod
    def import_shapes_from_file(filename):
        with open(filename, 'r') as file:
            return json.load(file)


class Runtime:
    _start = Any

    def start_nanoseconds(self):
        self._start = time_ns()

    def stop_nanoseconds(self):
        return (time_ns() - self._start) / 1_000_000  # from nanoseconds to milliseconds
