from validator.rule import Rule


class PositiveRule(Rule):
    def check(self, value):
        return value > 0
