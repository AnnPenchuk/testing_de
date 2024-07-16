import pytest

from src.Validation.valid import password_valid


def test_validate():
    password1 = 'qWer5%ty'
    assert password_valid(password1) is True