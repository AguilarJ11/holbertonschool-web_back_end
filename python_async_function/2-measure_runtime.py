#!/usr/bin/env python3

"""messure and return the runtime of wait_n function"""

import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """messure and return the runtime of wait_n function"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = start_time - end_time

    return total_time / n
