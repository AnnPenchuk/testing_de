import re

import pytest
from src.Validation.valid import Users_valid


def test_validate():
    password1 = 'qWer5%ty'
    password2 = '5qWer.t5'
    assert Users_valid.validate(password1) is None


