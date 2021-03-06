import pytest

from algorithms.math.rectangular_love import Rectangle, rectangular_love


@pytest.mark.math
def test_rectangular_love_good():
    rect1 = Rectangle((4, 8), (8, 4))
    rect2 = Rectangle((2, 10), (10, 2))
    assert rectangular_love(rect1, rect2) is True


@pytest.mark.math
def test_rectangular_love_bad():
    rect1 = Rectangle((4, 8), (8, 4))
    rect2 = Rectangle((0, 2), (2, 0))
    assert rectangular_love(rect1, rect2) is False


@pytest.mark.math
def test_rectangular_love_corner():
    rect1 = Rectangle((4, 8), (8, 4))
    rect2 = Rectangle((0, 4), (4, 0))
    assert rectangular_love(rect1, rect2) is True
