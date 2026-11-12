from abc import abstractmethod

from validator.rules import CustomRule


class Schema:
    def __init__(self, rule_factory, custom_rules):
        self.rule_factory = rule_factory
        self.rules = {}
        self.custom_rules = custom_rules
        self.is_required = False

    @abstractmethod
    def is_empty(self, value):
        pass

    def is_valid(self, value):
        if self.is_empty(value):
            return self.empty_result()
        for rule in self.rules.values():
            if not rule.check(value):
                return False
        return True

    def required(self):
        self.is_required = True
        return self

    def empty_result(self):
        return not self.is_required

    def test(self, func_name, arg):
        rule = CustomRule(self.custom_rules[func_name], arg)
        self.rules[func_name] = rule
        return self
