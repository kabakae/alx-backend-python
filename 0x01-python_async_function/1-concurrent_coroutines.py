#!/usr/bin/env python3
"""
This module contains asynchronous coroutines to simulate waiting for
random delays and gathering them in a sorted list.
"""

import asyncio
import random
from typing import List


async def wait_random(max_delay: int) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return
    the delay.

    Args:
        max_delay (int): The maximum number of seconds to wait.

    Returns:
        float: The actual delay in seconds.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return the
    list of all the delays in ascending order.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum number of seconds for each wait_random.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)

    # Sorting delays without using sort() directly
    sorted_delays = []
    for delay in delays:
        if not sorted_delays:
            sorted_delays.append(delay)
        else:
            inserted = False
            for i in range(len(sorted_delays)):
                if delay < sorted_delays[i]:
                    sorted_delays.insert(i, delay)
                    inserted = True
                    break
            if not inserted:
                sorted_delays.append(delay)

    return sorted_delays
