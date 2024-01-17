#!/usr/bin/env python3
"""a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measure Runtime Function """
    tasks = [async_comprehension() for _ in range(4)]

    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()

    return (end_time - start_time)
