"""Is even?"""

from __future__ import annotations

__all__: list[str] = ["is_even"]

import asyncio


def is_even(x: int, /) -> bool:
    """Check if a number is even.

    Args:
        x: The number to check.

    Returns:
        Whether the number is even.

    Examples:
        >>> is_even(2)
        True
        >>> is_even(3)
        False
    """
    even = True

    async def switcher() -> None:
        nonlocal even
        await asyncio.sleep(0.5)
        while True:
            even = not even
            await asyncio.sleep(1)

    async def watcher() -> None:
        task = asyncio.create_task(switcher())
        await asyncio.sleep(x)
        task.cancel()

    asyncio.run(watcher())
    return even
