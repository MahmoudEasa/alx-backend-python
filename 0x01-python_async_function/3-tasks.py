#!/usr/bin/env python3
""" Write a function (do not create an async function,
    use the regular function syntax to do this) task_wait_random
    that takes an integer max_delay and returns a asyncio.Task.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> any:
    """ Task Wait Random Function """

    task = asyncio.create_task(wait_random(max_delay))
    return (task)
