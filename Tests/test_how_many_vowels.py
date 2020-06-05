import pytest
from Code import how_many_vowels


def test_how_many_vowels():
    assert how_many_vowels.how_many_vowels("H") == 0
    assert how_many_vowels.how_many_vowels("HELLO") == 2
    assert how_many_vowels.how_many_vowels("Hello") == 2
    assert how_many_vowels.how_many_vowels("Hello World!!!") == 3
