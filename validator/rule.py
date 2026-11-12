from abc import abstractmethod


class Rule:
    @abstractmethod
    def check(self, value):
        pass
