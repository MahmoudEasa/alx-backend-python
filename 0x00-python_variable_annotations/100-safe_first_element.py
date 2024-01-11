#!/usr/bin/env python3
from typing import Union, Any, Sequence
""" Augment the following code with the correct duck-typed annotations: """


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ safe_first_element """
    if lst:
        return lst[0]
    else:
        return None
