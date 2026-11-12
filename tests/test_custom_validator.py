import operator

import pytest

from validator.validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_custom_string(validator):
    def start_with(value, start):
        return value.startswith(start)

    validator.add_validator("string", "startWith", start_with)
    schema = validator.string().test("startWith", "H")

    assert schema.is_valid("exlet") is False
    assert schema.is_valid("Hexlet") is True


def test_custom_number(validator):
    validator.add_validator("number", "min", operator.ge)
    schema = validator.number().test("min", 5)

    assert schema.is_valid(4) is False
    assert schema.is_valid(6) is True
