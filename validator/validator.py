import operator

from validator.string_schema import StringSchema


class Validator:
    def __init__(self):
        self.validators = {
            "string": {
                "contains": operator.contains,
                "min_len": lambda value, length: len(value) >= length,
            }
        }

    def string(self):
        return StringSchema(self.validators["string"].copy())
