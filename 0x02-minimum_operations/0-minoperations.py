#!/usr/bin/env python3
"""copy and paste operations."""


def minOperations(n):
    """a function to return the minimum number of copy past operations.
       Args:
           n(int): number of operations to be computed
    """
    if n <= 1:
        return 0
    operations = 0
    factor = 2
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    return operations
