#!/usr/bin/env python3

import asyncio
import time
from typing import List
from .1-async_comprehension import async_comprehension  # Relative import of async_comprehension

async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures the total runtime.
    
    Returns:
        The total runtime as a float.
    """
    start_time = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(), async_comprehension(), async_comprehension())
    end_time = time.perf_counter()
    
    return end_time - start_time
