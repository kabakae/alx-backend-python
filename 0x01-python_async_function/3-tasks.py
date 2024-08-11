#!/usr/bin/env python3
"""
This module contains a function that creates an asyncio.Task for
the wait_random coroutine from 0-basic_async_syntax.
"""

import asyncio
from basic_async_syntax import wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay for the wait_random coroutine.

    Returns:
        asyncio.Task: A task object wrapping the wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
