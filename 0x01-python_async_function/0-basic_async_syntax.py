#!/usr/bin/env python3

"""
This module provides an asynchronous function to simulate a delay.

It includes a single coroutine, `wait_random`, that waits for a random
amount of time between 0 and a specified maximum delay and then returns
the actual delay time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronously waits for a random amount of time and returns the delay.

    Args:
        max_delay (int): The maximum delay time in seconds (default is 10).

    Returns:
        float: The actual delay time in seconds.

    This function generates a random floating-point number between 0 and
    `max_delay`, waits for that duration asynchronously, and then returns
    the generated delay time.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
