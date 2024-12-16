#!/usr/bin/env python3
"""
Module containing the sum_list function.
"""


from typing import List

def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floats.

    Args:
        input_list (List[float]): A list containing float values.

    Returns:
        float: The sum of all float values in the list.
    """
    return sum(input_list)
