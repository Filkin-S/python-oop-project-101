from operator import contains

from validator.rule import Rule


class ContainsRule(Rule):
    def __init__(self, substr):
        self.substr = substr

    def check(self, value):
        return contains(value, self.substr)


class MinLenRule(Rule):
    def __init__(self, min_len):
        self.min_len = min_len

    def check(self, value):
        return len(value) >= self.min_len


class PositiveRule(Rule):
    def check(self, value):
        return value > 0


class RangeRule(Rule):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def check(self, value):
        return value in range(self.min_value, self.max_value + 1)


class SizeOfRule(Rule):
    def __init__(self, size):
        self.size = size

    def check(self, value):
        return len(value) == self.size


class ShapeRule(Rule):
    def __init__(self, shape):
        self.shape = shape

    def check(self, value):
        for key, schema in self.shape.items():
            if not schema.is_valid(value.get(key)):
                return False
        return True


class CustomRule(Rule):
    def __init__(self, func, arg):
        self.func = func
        self.arg = arg

    def check(self, value):
        return self.func(value, self.arg)
