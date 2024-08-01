#!/usr/bin/env python3
"""
8-make_multiplier Module
========================

This module contains the function `make_multiplier` which takes a float
multiplier as an argument and returns a function that multiplies a float b
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Parameters:
    -----------
    multiplier : float
        The multiplier to be used by the returned function.

    Returns:
    --------
    Callable[[float], float]
        A function that takes a float and returns the product of the float
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function
