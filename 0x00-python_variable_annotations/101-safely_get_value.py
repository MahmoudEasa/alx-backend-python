#!/usr/bin/env python3
""" Given the parameters and the return values,
    add type annotations to the function
"""
from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None) ->\
                     Union[Any, TypeVar('T')]:
    """ Safely Get Value Function"""
    if key in dct:
        return dct[key]
    else:
        return default
