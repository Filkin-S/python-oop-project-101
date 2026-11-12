from validator.schema import Schema


class NumberSchema(Schema):
    def is_empty(self, value):
        return value is None

    def positive(self):
        rule = self.rule_factory.create_rule("positive")
        self.rules["positive"] = rule
        return self

    def range(self, min_val, max_val):
        rule = self.rule_factory.create_rule("range", min_val, max_val)
        self.rules["range"] = rule
        return self
