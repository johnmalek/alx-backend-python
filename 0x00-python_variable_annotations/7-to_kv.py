#!/usr/bin/env python3
"""
A function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A functiont that takes argumrnts and returns a tuple
    k: a string argument
    returns:
        a tuple
    """
    return (k, v**2)
