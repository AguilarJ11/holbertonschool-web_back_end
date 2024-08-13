#!/usr/bin/env python3

"""function that thakes integers and floats
and returns their sum as a float."""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """function that thakes integers and floats
    and returns their sum as a float."""
    res: float = 0.0
    for num in mxd_list:
        res += num
    return res
