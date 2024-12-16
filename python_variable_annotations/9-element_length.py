#!/usr/bin/env python3
"""
Module containing the element_length function.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples,
    where each tuple contains an element from the input
    iterable and the length of that element.

    Args:
        lst (Iterable[Sequence]):
        An iterable containing sequences (e.g., lists, strings).

    Returns:
        List[Tuple[Sequence, int]]:
        A list of tuples with each sequence and its length.
    """
    return [(i, len(i)) for i in lst]
