#!/usr/bin/env python3

"""function that returns their sum as a float"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """function that returns their sum as a float"""
    res: float = 0.0
    for num in input_list:
        res += num
    return res
