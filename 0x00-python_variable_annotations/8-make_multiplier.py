#!/usr/bin/env python3
""" Write a type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function that
    multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make multiplier Function """
    def fun(mul: float) -> float:
        """ Function to multiplies a float by multiplier """
        return (mul * multiplier)
    return (fun)
