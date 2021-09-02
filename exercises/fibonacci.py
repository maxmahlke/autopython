#!/usr/bin/env python3
from functools import lru_cache
import time


@lru_cache
def fibonacci(n):
    """Compute the value of the Fibonacci number F_n.

    Parameters
    ==========
    n : int
        The index of the Fibonacci number to compute.

    Returns
    =======
    float
        The value of the nth Fibonacci number.
    """

    # Check the input
    if not isinstance(n, int):
        raise TypeError(f"n has to be of type int, received {type(n)}.")

    # Compute the value recursively
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":

    # Store the start time of the computation
    start = time.time()

    # Compute the sequence value
    n = 40
    F_n = fibonacci(n)

    # Print the value and the execution time
    print(f"F_{n} = {F_n}. It took {time.time() - start}s to compute this.")
