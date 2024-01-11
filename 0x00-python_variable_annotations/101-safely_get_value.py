#!/usr/bin/env python3
from typing import Union, Mapping, Any, TypeVar


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[TypeVar('T'), None] = None) ->\
                     Union[Any, TypeVar('T')]:
    if key in dct:
        return dct[key]
    else:
        return default
