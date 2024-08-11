#!/usr/bin/env python3
import time
import asyncio
from 1-concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Execute wait_n with the provided arguments
    end_time = time.time()  # Record the end time
    
    total_time = end_time - start_time  # Calculate the total elapsed time
    return total_time / n  # Return the average time per coroutine

# You can test the function with the provided values in 2-main.py
if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
