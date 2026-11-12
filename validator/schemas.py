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


class ListSchema(Schema):
    def is_empty(self, value):
        return value is None

    def sizeof(self, size):
        rule = self.rule_factory.create_rule("sizeof", size)
        self.rules["sizeof"] = rule
        return self
