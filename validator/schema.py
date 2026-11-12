from abc import abstractmethod


class Schema:
    def __init__(self, rule_factory, custom_rules):
        self.rule_factory = rule_factory
        self.rules = {} | custom_rules
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
