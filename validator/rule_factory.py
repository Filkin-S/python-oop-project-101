from validator.contains_rule import ContainsRule
from validator.min_len_rule import MinLenRule
from validator.positive_rule import PositiveRule
from validator.range_rule import RangeRule


class RuleFactory:
    def __init__(self):
        self.rules = {
            "contains": ContainsRule,
            "min_len": MinLenRule,
            "positive": PositiveRule,
            "range": RangeRule,
        }

    def create_rule(self, rule_name, *args, **kwargs):
        return self.rules[rule_name](*args, **kwargs)
