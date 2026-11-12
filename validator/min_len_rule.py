from validator.rule import Rule


class MinLenRule(Rule):
    def __init__(self, min_len):
        self.min_len = min_len

    def check(self, value):
        return len(value) >= self.min_len
