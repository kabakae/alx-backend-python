#!/usr/bin/env python3
"""
2-floor Module
==============

This module contains the function `floor` which takes a float as an argument
and returns the floor of the float.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of the float.

    Parameters:
    -----------
    n : float
        The float number to floor.

    Returns:
    --------
    int
        The floor of the float.
    """
    return math.floor(n)
