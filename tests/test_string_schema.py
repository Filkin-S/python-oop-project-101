import pytest

from validator.validator import Validator


@pytest.fixture()
def string_validator():
    v = Validator()
    return v.string()


def test_empty(string_validator):
    assert string_validator.is_valid("") is True
    assert string_validator.is_valid(None) is True
    string_validator.required()
    assert string_validator.is_valid("") is False
    assert string_validator.is_valid(None) is False


def test_contains(string_validator):
    string_validator.contains("es")
    assert string_validator.is_valid("Test") is True
    assert string_validator.is_valid("Tst") is False


def test_min_len(string_validator):
    string_validator.min_len(5)
    assert string_validator.is_valid("Test1") is True
    assert string_validator.is_valid("Test") is False


def test_combined(string_validator):
    string_validator.required().contains("T").min_len(5)
    assert string_validator.is_valid("Test1") is True
    assert string_validator.is_valid("Test") is False
    assert string_validator.is_valid("") is False
    assert string_validator.is_valid("test1") is False


def test_double_call(string_validator):
    string_validator.min_len(5).min_len(4)
    assert string_validator.is_valid("Test") is True


def test_indep_schemas(string_validator):
    other_schema = Validator().string()
    assert string_validator.is_valid("") is True
    assert other_schema.is_valid("") is True
    other_schema.required()
    assert string_validator.is_valid("") is True
    assert other_schema.is_valid("") is False
