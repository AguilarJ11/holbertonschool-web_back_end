#!/usr/bin/env python3

import random, asyncio

"""Return a random number between 0 and max_delay(def 10)"""


async def wait_random(max_delay: int = 10) -> float:
    """Return a random number between 0 and max_delay(def 10)"""
    print("Picking a random number...")
    await asyncio.sleep(1)
    return print(random.uniform(0, max_delay))

asyncio.run(wait_random())