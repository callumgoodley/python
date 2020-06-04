import pytest
from Code import centered_average


def test_centered_average():
    assert centered_average.centered_average([1, 2, 3, 4, 100]) == 3
    assert centered_average.centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
    assert centered_average.centered_average([-10, -4, -2, -4, -2, 0]) == - 3
