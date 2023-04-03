#!/usr/bin/env python3
"""
Async coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int=10) -> float:
    """
    an asynchronous coroutine that takes in an integer argument
    that waits for a random delay between 0 and max_delay  seconds
    and eventually returns it.
    max_delay: an argument of type int
    return:
        The time in seconds between 0 and max_delay
    """
    i = random.randint(0, max_delay)
    await asyncio.sleep(i)
    return i
