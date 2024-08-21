#!/usr/bin/env python3

""""""

async_generator = __import__('0-async_generator').async_generator
import random
import asyncio


async def async_comprehension():
    random_numbers = []
    async for i in async_generator():
        random_numbers.append(i)
    return random_numbers