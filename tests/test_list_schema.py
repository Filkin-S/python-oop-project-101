import pytest

from validator.validator import Validator


@pytest.fixture()
def list_validator():
    v = Validator()
    return v.list()


def test_list(list_validator):
    assert list_validator.is_valid([1]) is True


def test_empty(list_validator):
    assert list_validator.is_valid([]) is True
    assert list_validator.is_valid(None) is True
    list_validator.required()
    assert list_validator.is_valid([]) is True
    assert list_validator.is_valid(None) is False


def test_sizeof(list_validator):
    list_validator.sizeof(2)
    assert list_validator.is_valid([]) is False
    assert list_validator.is_valid(["test"]) is False
    assert list_validator.is_valid([1, "test"]) is True
