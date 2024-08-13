#!/usr/bin/env python3

"""takes a float multiplier as argument and returns
a function that multiplies a float by multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a float multiplier as argument and returns
    a function that multiplies a float by multiplier"""

    def multi_function(n: float) -> float:
        return n * multiplier

    return multi_function
