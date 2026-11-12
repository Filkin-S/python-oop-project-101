import pytest

from validator.validator import Validator


@pytest.fixture()
def validator():
    return Validator()


def test_dict(validator):
    dict_validator = validator.dict()
    dict_validator.shape(
        {
            "name": validator.string().required(),
            "age": validator.number().positive(),
        }
    )
    assert dict_validator.is_valid({"name": "kolya", "age": 100}) is True
    assert dict_validator.is_valid({"name": "maya", "age": None}) is True
    assert dict_validator.is_valid({"name": "", "age": None}) is False
    assert dict_validator.is_valid({"name": "ada", "age": -5}) is False
