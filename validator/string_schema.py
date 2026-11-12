from validator.schema import Schema


class StringSchema(Schema):
    def is_empty(self, value):
        return value is None or value == ""

    def contains(self, substr):
        rule = self.rule_factory.create_rule("contains", substr)
        self.rules["contains"] = rule
        return self

    def min_len(self, length):
        rule = self.rule_factory.create_rule("min_len", length)
        self.rules["min_len"] = rule
        return self
