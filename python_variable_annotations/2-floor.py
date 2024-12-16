#!/usr/bin/env python3
"""
Module containing the floor function.
"""


import math


def floor(n: float) -> int:
    """
    Returns the floor value of a float.

    Args:
        n (float): The input float number.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)
