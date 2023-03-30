#!/usr/bin/env python3
"""
A function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    A function that accepts a list and returns the sum of values in it
    input_list: list with the values
    returns:
        sum of values in list
    """
    list_sum: float = 0
    for value in input_list:
        list_sum += value
    return list_sum
