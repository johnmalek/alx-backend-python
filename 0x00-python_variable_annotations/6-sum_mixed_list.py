#!/usr/bin/env python3
"""
A function
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    A function that accepts a list of integers and floats
    and returns their sum
    mxd_list: the input list
    returns:
        sum as a float
    """
    sum_list: float = 0.0
    for value in mxd_lst:
        sum_list += value
    return sum_list
