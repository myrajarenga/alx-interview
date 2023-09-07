#!/usr/bin/env python3

"""
function to calculate winner of game of 
prime numbers
"""


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

    def generate_primes(n):
        primes = [True for _ in range(1, n + 1, 1)]
        primes[0] = False
        for i, is_prime in enumerate(primes, 1):
            if i == 1 or not is_prime:
                continue
            for j in range(i + i, n + 1, i):
                primes[j - 1] = False
        return primes

    for _, n in zip(range(x), nums):
        primes = generate_primes(n)
        primes_count = len(list(filter(lambda x: x, primes[0: n])))
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None

    return 'Maria' if marias_wins > bens_wins else 'Ben'
