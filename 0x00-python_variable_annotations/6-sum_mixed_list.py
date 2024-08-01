#!/usr/bin/env python3
"""
6-sum_mixed_list Module
=======================

This module contains the function `sum_mixed_list` which takes a list of
integers and floats as an argument and returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Parameters:
    -----------
    mxd_lst : List[Union[int, float]]
        The list of integers and floats to sum.

    Returns:
    --------
    float
        The sum of the list of integers and floats.
    """
    return sum(mxd_lst)
