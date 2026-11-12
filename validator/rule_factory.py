from validator.rules import (
    ContainsRule,
    MinLenRule,
    PositiveRule,
    RangeRule,
    ShapeRule,
    SizeOfRule,
)


class RuleFactory:
    def __init__(self):
        self.rules = {
            "contains": ContainsRule,
            "min_len": MinLenRule,
            "positive": PositiveRule,
            "range": RangeRule,
            "sizeof": SizeOfRule,
            "shape": ShapeRule,
        }

    def create_rule(self, rule_name, *args, **kwargs):
        return self.rules[rule_name](*args, **kwargs)
