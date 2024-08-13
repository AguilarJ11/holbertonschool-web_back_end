#!/usr/bin/env python3

"""function that returns their sum as a float"""


def sum_list(input_list: list[float]) -> float:
    """function that returns their sum as a float"""
    res: float = 0
    for num in input_list:
        res += num
    return res
