from validator.rule_factory import RuleFactory
from validator.schemas import (
    DictSchema,
    ListSchema,
    NumberSchema,
    StringSchema,
)


class Validator:
    def __init__(self):
        self.custom_rules = {
            "string": {},
            "number": {},
            "list": {},
            "dict": {},
        }
        self.rule_factory = RuleFactory()

    def string(self):
        return StringSchema(self.rule_factory, self.custom_rules["string"])

    def number(self):
        return NumberSchema(self.rule_factory, self.custom_rules["number"])

    def list(self):
        return ListSchema(self.rule_factory, self.custom_rules["list"])

    def dict(self):
        return DictSchema(self.rule_factory, self.custom_rules["dict"])
