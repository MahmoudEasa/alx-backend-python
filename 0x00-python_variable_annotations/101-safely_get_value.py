#!/usr/bin/env python3
from typing import Union, Mapping, Any, TypeVar
""" Given the parameters and the return values,
    add type annotations to the function
"""


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None) ->\
                     Union[Any, TypeVar('T')]:
    """ safely_get_value """
    if key in dct:
        return dct[key]
    else:
        return default
