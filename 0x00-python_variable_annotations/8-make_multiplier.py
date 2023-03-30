#!/usr/bin/env python3
"""
A function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that takes an argument and returns a function
    multiplier: argument to be multiplied
    returns:
        a function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
