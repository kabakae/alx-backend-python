#!/usr/bin/env python3
import time
import asyncio
from typing import List
from 1_concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Measures the average runtime of wait_n."""
    start_time = time.time()  # Start time
    asyncio.run(wait_n(n, max_delay))  # Run wait_n
    end_time = time.time()  # End time
    
    total_time = end_time - start_time  # Calculate the total time
    return total_time / n  # Return the average time per coroutine

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
