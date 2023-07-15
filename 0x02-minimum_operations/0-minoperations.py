#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """ return number of minimal operations"""
    if n <= 1:
        return 0

    i = 2

    while i <= int(n ** 0.5):
        if n % i == 0:
            return i + minOperations(n // i)
        i += 1

    return n
