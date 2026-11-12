from validator.rule import Rule


class RangeRule(Rule):
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value

    def check(self, value):
        return value in range(self.min_value, self.max_value + 1)
