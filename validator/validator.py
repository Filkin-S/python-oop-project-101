from validator.rule_factory import RuleFactory
from validator.schemas import ListSchema, NumberSchema, StringSchema


class Validator:
    def __init__(self):
        self.custom_rules = {
            "string": {},
            "number": {},
            "list": {},
        }
        self.rule_factory = RuleFactory()

    def string(self):
        return StringSchema(self.rule_factory, self.custom_rules["string"])

    def number(self):
        return NumberSchema(self.rule_factory, self.custom_rules["number"])

    def list(self):
        return ListSchema(self.rule_factory, self.custom_rules["list"])
