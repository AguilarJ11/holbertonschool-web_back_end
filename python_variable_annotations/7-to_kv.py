#!/usr/bin/env python3

from typing import Union, Tuple

"""function that takes a string k and an int OR float v as arguments and
returns a tuplewith the values of v added"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """function that takes a string k and an int OR float v as arguments and
    returns a tuplewith the values of v added"""

    return (k, v * v)
