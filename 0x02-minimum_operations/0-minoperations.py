#!/usr/bin/python3
"""Min Operations Algorithm

This script contains a function `minOperations` that calculates the minimum
number of operations required to print exactly `n` 'H' characters in a file.
The allowed operations are:
1. Copy All: Copy all the characters present in the file.
2. Paste: Paste the characters that were copied.

The function uses prime factorization to determine the minimum number of
operations needed.

Functions:
    minOperations(n): Returns the minimum number of operations to
    print `n` 'H' characters.
"""

import math


def minOperations(n):
    """Function to find the minimum operations to print exactly `n` 'H'
    characters in a file.

    Args:
        n (int): The number of 'H' characters to be printed.

    Returns:
        int: The minimum number of operations required to print `n` 'H'
        characters.
            0 if `n` is less than or equal to 1.
    """
    if n <= 1:
        return 0

    prime_factors = []

    # Extract the number of 2s that divide `n`
    while n % 2 == 0:
        prime_factors.append(2)
        n = n // 2

    # `n` must be odd at this point, so we can skip even numbers
    for i in range(3, int(math.sqrt(n) + 1), 2):
        # While `i` divides `n`, add `i` and divide `n`
        while n % i == 0:
            prime_factors.append(i)
            n = n // i

    # This condition is to check if `n` is a prime number greater than 2
    if n > 2:
        prime_factors.append(n)

    return sum(prime_factors)
