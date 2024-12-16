#!/usr/bin/env python3
""" Module containing the to_kv function.
		Takes a string k and an int OR float v as arguments and returns a tuple.
		The first element of the tuple is the string k. The second element is the square of the int/float v.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
		"""
		Returns a tuple containing the string k and the square of the int/float v.

		Args:
				k (str): The string key.
				v (Union[int, float]): The int or float value.

		Returns:
				Tuple[str, float]: A tuple containing k and the square of v.
		"""
		return (k, v * v)
