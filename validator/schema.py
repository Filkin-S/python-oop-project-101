from abc import abstractmethod


class Schema:
    def __init__(self, validators):
        self.validators = validators
        self.rules = {}
        self.is_required = False

    @abstractmethod
    def is_valid(self, value):
        pass

    def required(self):
        self.is_required = True
        return self
