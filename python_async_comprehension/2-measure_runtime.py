#!/usr/bin/env python3

"""mesure the run time of an async function 4 times"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:

    """mesure the run time of an async function 4 times"""

    start_time = time.perf_counter()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.perf_counter()
    total_time = end_time - start_time

    return total_time
