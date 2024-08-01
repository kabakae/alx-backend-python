#!/usr/bin/env python3
"""
7-to_kv Module
==============

This module contains the function `to_kv` which takes a string and an integer
or float as arguments and returns a tuple. The first element of the tuple is the
string, and the second element is the square of the integer/float, annotated as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is the string k, and the second element
    is the square of the int/float v, represented as a float.

    Parameters:
    -----------
    k : str
        The string element of the tuple.
    v : Union[int, float]
        The integer or float to be squared.

    Returns:
    --------
    Tuple[str, float]
        A tuple containing the string k and the square of v as a float.
    """
    return (k, float(v ** 2))
