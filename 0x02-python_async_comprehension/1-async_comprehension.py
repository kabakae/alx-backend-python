#!/usr/bin/env python3

from typing import List
from async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers between 0 and 10 using an
    asynchronous comprehension over the async_generator.
    
    Returns:
        List of 10 random float numbers.
    """
    return [number async for number in async_generator()][:10]
