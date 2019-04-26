import pytest

from algorithms.basic import fibonacci as fib


@pytest.mark.dynamic
class TestFibonacci:
    @pytest.mark.parametrize(
        "func",
        [
            fib.fibonacci_iterative,
            fib.fibonacci_recursive,
            fib.fibonacci_stack,
            fib.fibonacci_dp_bottom,
            fib.fibonacci_dp_top,
        ],
    )
    @pytest.mark.parametrize(
        "i,o", [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5), (6, 8)]
    )
    def test_fibonacci(self, func, i, o):
        assert func(i) == o
