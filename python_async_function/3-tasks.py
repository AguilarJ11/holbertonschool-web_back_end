#!/usr/bin/env python3

"""Create a task an return it"""

wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Create a task an return it"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
