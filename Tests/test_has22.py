import pytest
from Code import has22


def test_answer():
    assert has22.has22([1, 2, 3]) == False
    assert has22.has22([2, 2, 0]) == True
