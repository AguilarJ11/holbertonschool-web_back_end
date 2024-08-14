#!/usr/bin/env python3

"""Execute n times the wait_random
function with the max_delay for arg
and return a list of those random numbers"""

from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Execute n times the wait_random
    function with the max_delay for arg
    and return a list of those random numbers"""
    random_list = []
    for times in range(n):
        delay = await task_wait_random(max_delay)
        random_list.append(delay)

    random_list.sort()
    return random_list
