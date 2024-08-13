#!/usr/bin/env python3

"""Function that take an iterable and return a list of tuples
each value of the tuples is an iterable and the lenght"""

from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function that take an iterable and return a list of tuples
    each value of the tuples is an iterable and the lenght"""
    return [(i, len(i)) for i in lst]
