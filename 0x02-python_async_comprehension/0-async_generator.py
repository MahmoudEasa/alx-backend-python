#!/usr/bin/env python3
""" The coroutine will loop 10 times, each time asynchronously wait 1 second,
    then yield a random number between 0 and 10. Use the random module
"""
from random import randint
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """ Async Generator Function """
    for i in range(10):
        await asyncio.sleep(1)
        yield randint(0, 10)
