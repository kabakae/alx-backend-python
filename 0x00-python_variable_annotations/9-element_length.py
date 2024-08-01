#!/usr/bin/env python3
"""
9-element_length Module
=======================

This module contains the function `element_length` which takes an iterable of
sequences as an argument and returns a list of tuples. Each tuple contains a 
sequence and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples where each tuple contains a sequence from thut
    iterable and its length.

    Parameters:
    -----------
    lst : Iterable[Sequence]
        The iterable of sequences to process.

    Returns:
    --------
    List[Tuple[Sequence, int]]
        A list of tuples, each containing a sequence from the input iterable a
    """
    return [(i, len(i)) for i in lst]
