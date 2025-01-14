"""Testing for sleep-even."""

import pytest
from pytest_benchmark.fixture import BenchmarkFixture  # type: ignore[import]

from sleep_even import is_even


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (2, True),
        (3, False),
    ],
)
def test_is_even(
    benchmark: BenchmarkFixture,
    value: int,
    *,
    expected: bool,
) -> None:
    """Test `is_even`."""
    result = benchmark(is_even, value)
    assert result == expected
