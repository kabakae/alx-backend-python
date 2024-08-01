#!/usr/bin/env python3
"""
101-safely_get_value Module
===========================

This module contains the function `safely_get_value` which safely re a value
from a dictionary given a key, with an optional default value.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from the dictionary `dct` usi `key`. If the key
    is not present, returns the `default` value.

    Parameters:
    -----------
    dct : Mapping
        The dictionary from which to retrieve the value.
    key : Any
        The key to look up in the dictionary.
    default : Union[T, None], optional
        The default value to return if the key is not found (default is No).

    Returns:
    --------
    Union[Any, T]
        The value from the dictionary if the key is found, otherwise the `de
    """
    if key in dct:
        return dct[key]
    else:
        return default
