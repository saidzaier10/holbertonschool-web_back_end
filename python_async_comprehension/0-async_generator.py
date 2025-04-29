#!/usr/bin/env python3
"""
Module for asynchronous random number generation
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    Coroutine that generates random numbers asynchronously.

    Yields 10 random numbers between 0 and 10,
    waiting 1 second between each number.

    Yields:
        float: Random number between 0 and 10
    """
    # Loop 10 times
    for _ in range(10):
        # Wait for 1 second asynchronously
        await asyncio.sleep(1)
        # Generate and yield a random float between 0 and 10
        yield random.uniform(0, 10)
