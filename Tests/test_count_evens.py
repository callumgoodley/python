import pytest
from Code import count_evens


def test_count_evens():
    assert count_evens.count_evens([]) == 0
    assert count_evens.count_evens([0]) == 1
    assert count_evens.count_evens([1]) == 0
    assert count_evens.count_evens([1, 2]) == 1
    assert count_evens.count_evens([1, 1]) == 0
    assert count_evens.count_evens([2, 2]) == 2
