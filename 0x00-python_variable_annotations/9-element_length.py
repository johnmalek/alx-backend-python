#!/usr/bin/env python3
"""
A function
"""
from typing import Iterable, Tuple, Sequence, List



def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    A function that computes the length of sequences
    """
    return [(i, len(i)) for i in lst]
