"""Benchmarking for sleep-even."""

from sleep_even import is_even


class TimeSuite:
    """A benchmark suite for timing sleep-even."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `value` attribute."""
        self.value = 3

    def time_make_greeting(self) -> None:
        """Benchmark the `is_even` function for its execution time."""
        is_even(self.value)


class MemSuite:
    """A benchmark suite for measuring the memory usage of sleep-even."""

    def setup(self) -> None:
        """Set up the benchmark by initializing the `value` attribute."""
        self.value = 3

    def mem_make_greeting(self) -> bool:
        """Benchmark the `is_even` function for its memory usage."""
        return is_even(self.value)
