#!/usr/bin/env python3

"""Loop 10 times and wait 1 second per loop, then yield a random number
between 0 and 10"""

from typing import AsyncGenerator
import random
import asyncio


async def async_generator() -> AsyncGenerator[float, None]:
    """Loop 10 times and wait 1 second per loop, then yield a random number
    between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
