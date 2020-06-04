import pytest
from Code import cotd_3


def test_cotd_3():
    assert cotd_3.generate_dictionary_param_input(
        8) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
