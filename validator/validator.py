from validator.number_schema import NumberSchema
from validator.rule_factory import RuleFactory
from validator.string_schema import StringSchema


class Validator:
    def __init__(self):
        self.custom_rules = {
            "string": {},
            "number": {},
        }

    def string(self):
        return StringSchema(RuleFactory(), self.custom_rules["string"])

    def number(self):
        return NumberSchema(RuleFactory(), self.custom_rules["number"])
