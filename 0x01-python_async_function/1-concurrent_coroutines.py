#!/usr/bin/env python3
"""
A coroutine
"""
wait_random = __import__('0-basic_async_syntax').wait_random
import async
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    A coroutine that spawns wait_random n time
    n: first int argument
    max_delay: second int argument
    returns:
        list of all delays
    """
    no_of_waits = await asyncio.gather(wait_random(max_delay, range(n)))
    return no_of_waits

