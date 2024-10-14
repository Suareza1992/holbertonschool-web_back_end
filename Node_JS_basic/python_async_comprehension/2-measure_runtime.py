#!/usr/bin/env python3

'''measure_runtime is a coroutine that will
execute async_comprehension four times in parallel.'''


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures total runtime of executing async_comprehension.'''
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
