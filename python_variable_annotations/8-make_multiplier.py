#!/usr/bin/env python3
"""
Module containing the make_multiplier function.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]:
        A function that takes a float and returns the product.
    """
    def multiplier_function(x: float) -> float:
        """
        Multiplies the input float by the multiplier.

        Args:
            x (float): The input value.

        Returns:
            float: The result of multiplying x by the multiplier.
        """
        return x * multiplier

    return multiplier_function
