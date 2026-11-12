from operator import contains

from validator.rule import Rule


class ContainsRule(Rule):
    def __init__(self, substr):
        self.substr = substr

    def check(self, value):
        return contains(value, self.substr)
