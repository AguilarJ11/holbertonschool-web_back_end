#!/usr/bin/env python3

"""Return a random number between 0 and max_delay(def 10)"""

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Return a random number between 0 and max_delay(def 10)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
