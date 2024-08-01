#!/usr/bin/env python3
"""
100-safe_first_element Module
=============================

This module contains the function `safe_first_element` which safely retrieves
the first element of a sequence, returning None if the sequence is empty.
"""

from typing import Any, Sequence, Union

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element of the sequence `lst`. If the sequence is
    empty, returns None.

    Parameters:
    -----------
    lst : Sequence[Any]
        The sequence from which to retrieve the first element.

    Returns:
    --------
    Union[Any, None]
        The first element of the sequence if it is not empty, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
