#!/usr/bin/env python3
"""
Module containing the sum_mixed_list function.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list of integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]):
        A list containing integers and floats.

    Returns:
        float: The sum of all values in the list as a float.
    """
    return sum(mxd_lst)
