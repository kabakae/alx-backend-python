#!/usr/bin/env python3
"""
Module containing the async_comprehension coroutine.
"""

from typing import List
import asyncio
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension
    over async_generator, then returns the 10 random numbers.
    """
    return [i async for i in async_generator()]
