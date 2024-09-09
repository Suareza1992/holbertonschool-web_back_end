#!/usr/bin/env python3

"""
Write a type-annotated function make_multiplier that takes
a float muliplier as an argument and returns a function that
multiplies a float by multiplier.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Make a multipler """
    return lambda a: a * multiplier
