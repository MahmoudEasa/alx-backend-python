#!/usr/bin/env python3


def zoom_array(lst: tuple, factor: int = 2) -> list:
    zoomed_in: list = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
