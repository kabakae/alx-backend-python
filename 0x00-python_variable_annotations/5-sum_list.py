#!/usr/bin/env python3
"""
5-sum_list Module
=================

This module contains the function `sum_list` which takes a list of floats as
an argument and returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Parameters:
    -----------
    input_list : List[float]
        The list of floats to sum.

    Returns:
    --------
    float
        The sum of the list of floats.
    """
    return sum(input_list)
