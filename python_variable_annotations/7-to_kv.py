#!/usr/bin/env python3
"""
Module containing the to_kv function.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple where the first element is a string and the second is
    the square of the given int/float value.

    Args:
        k (str): The input string.
        v (Union[int, float]): The input value, either an int or a float.

    Returns:
        Tuple[str, float]: A tuple containing the string and
        the square of the value as a float.
    """
    return (k, float(v ** 2))
