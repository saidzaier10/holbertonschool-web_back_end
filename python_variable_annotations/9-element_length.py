#!/usr/bin/env python3
""" module contenant the element_lenght function"""


from typing import List, Union, Tuple


def element_length(lst: List[Union[int, str]]) -> List[Tuple[Union[int, str], int]]:
"""return a list of tuples containing the element and its length
Args: lst: List[Union[int, str]]: list of integers and strings
Returns: List[Tuple[Union[int, str], int]]: list of tuples containing the element and its length
"""
		return [(i, len(i)) for i in lst]
