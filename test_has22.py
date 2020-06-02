import pytest
from has22 import has22


def test_answer():
    assert has22([1, 2, 3]) == False
    assert has22([2, 2, 0]) == True
