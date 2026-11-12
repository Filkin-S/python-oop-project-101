import pytest

from validator.validator import Validator


@pytest.fixture()
def number_validator():
    v = Validator()
    return v.number()


def test_number(number_validator):
    assert number_validator.is_valid(2) is True


def test_empty(number_validator):
    assert number_validator.is_valid(None) is True
    number_validator.required()
    assert number_validator.is_valid(None) is False


def test_positive(number_validator):
    number_validator.positive()
    assert number_validator.is_valid(-2) is False
    assert number_validator.is_valid(2) is True


def test_range(number_validator):
    number_validator.range(-2, 3)
    assert number_validator.is_valid(3) is True
    assert number_validator.is_valid(4) is False


def test_range_positive(number_validator):
    number_validator.range(-1, 1).positive()
    assert number_validator.is_valid(-1) is False
    assert number_validator.is_valid(1) is True
    assert number_validator.is_valid(2) is False
