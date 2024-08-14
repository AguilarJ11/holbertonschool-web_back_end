#!/usr/bin/env python3

"""Create a task an return it"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task an return it"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
