#!/usr/bin/env python3
""" Take the code from wait_n and alter it into
    a new function task_wait_n.
    The code is nearly identical to wait_n except
    task_wait_random is being called.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Task Wait N Function """
    delays: List[float] = []

    async def wait_append():
        """ Append to list """
        delay: asyncio.Task = await task_wait_random(max_delay)
        delays.append(delay)

    tasks: List = [wait_append() for _ in range(n)]
    await asyncio.gather(*tasks)
    return (delays)
