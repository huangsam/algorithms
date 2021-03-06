import pytest

from algorithms.math import factorial as fact


@pytest.mark.math
@pytest.mark.dynamic
@pytest.mark.parametrize(
    "func",
    [
        fact.factorial_recursive,
        fact.factorial_stack,
        fact.factorial_dp_bottom,
        fact.factorial_dp_top,
    ],
)
@pytest.mark.parametrize("i,o", [(0, 1), (1, 1), (2, 2), (3, 6), (4, 24), (5, 120)])
def test_factorial(func, i, o):
    assert func(i) == o
