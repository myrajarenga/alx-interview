#!/usr/bin/python3
"""
minimum operations
"""


def minOperations(n):
    """ return number of minimal operations"""
    if n < 2:
        return 0

    operations = 0
    current = 1

    while current != n:
        if n % current == 0:
            operations += 1
            current *= 2

            if current == n:
                break
        operations += 1
        current += current

    return operations
