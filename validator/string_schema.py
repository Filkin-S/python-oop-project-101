from validator.schema import Schema


class StringSchema(Schema):
    def is_valid(self, value):
        if value is None or value == "":
            return True if not self.is_required else False
        for name, arg in self.rules.items():
            func = self.validators[name]
            if not func(value, arg):
                return False
        return True

    def contains(self, substr):
        self.rules["contains"] = substr
        return self

    def min_len(self, length):
        self.rules["min_len"] = length
        return self
