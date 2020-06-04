import pytest
from Code import make_bricks


def test_make_bricks():
    assert make_bricks.make_bricks(3, 1, 8)
    assert make_bricks.make_bricks(3, 1, 9) == False
    assert make_bricks.make_bricks(3, 2, 10) == True
    assert make_bricks.make_bricks(3, 2, 8) == True
    assert make_bricks.make_bricks(3, 2, 9) == False
    assert make_bricks.make_bricks(6, 1, 11) == True
    assert make_bricks.make_bricks(6, 0, 11) == False
    assert make_bricks.make_bricks(1, 4, 11) == True
    assert make_bricks.make_bricks(0, 3, 10) == True
    assert make_bricks.make_bricks(1, 4, 12) == False
    assert make_bricks.make_bricks(3, 1, 7) == True
    assert make_bricks.make_bricks(1, 1, 7) == False
    assert make_bricks.make_bricks(1000000, 1000, 1000100) == True
    assert make_bricks.make_bricks(2, 1000000, 100003) == False
    assert make_bricks.make_bricks(20, 0, 19) == True
    assert make_bricks.make_bricks(20, 0, 21) == False
    assert make_bricks.make_bricks(20, 4, 51) == False
    assert make_bricks.make_bricks(20, 4, 39) == True
