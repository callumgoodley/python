import pytest
from Code import classes


def test_classes():
    assert classes.Callum.scores(1, 2, 3) == 2
    assert classes.John.scores(5, 5, 5) == 5
