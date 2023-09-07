#!/usr/bin/env python3

"""
function to calculate winner of game of 
prime numbers
"""


def sieve_of_eratosthenes(n):
    """The function sieve_of_eratosthenes(n) implements the Sieve of Eratosthenes algorithm, 
    which is an ancient and efficient method for finding all prime numbers up to a given limit n.
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            primes[i*i : n+1 : i] = [False] * len(primes[i*i : n+1 : i])
    return primes

def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a game based on prime number selection.

    Args:
        x (int): Number of rounds.
        nums (list): List of integers representing the upper limits for each round.

    Returns:
        str or None: Name of the player with the most wins. Returns None if the winner cannot be determined.
    """

    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    for _, n in zip(range(x), nums):
        primes = sieve_of_eratosthenes(n)
        primes_count = sum(primes[2:n+1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
