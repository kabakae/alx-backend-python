#!/usr/bin/env python3
"""
Module containing the async_generator coroutine.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that yields a random number between 0 and 10 asynchronously 1
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
