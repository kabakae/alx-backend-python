#!/usr/bin/env python3
"""
This module contains a function to measure the execution time of the
wait_n coroutine from 1-concurrent_coroutines.py.
"""


import asyncio
import time
from typing import List
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time for wait_n(n, max_delay) and return
    the average time per coroutine.

    Args:
        n (int): The number of times to call wait_n.
        max_delay (int): The maximum delay for wait_n.

    Returns:
        float: The average time per coroutine in seconds.
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
   

    total_time = end_time - start_time
    average_time = total_time / n
    
    return average_time
