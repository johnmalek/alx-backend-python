#!/usr/bin/env python3
"""
A coroutine
"""
import asyncio
import time


wait = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures an approximate elapsed time
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
