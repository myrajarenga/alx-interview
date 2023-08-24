#!/usr/bin/python3
"""
change modeule
"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    """
    Create an array to store the minimum number of
    coins needed for each amount.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    """
    Iterate through each coin and calculate the
    minimum coins needed for each amount.
    """
    for coin_value in coins:
        for amount in range(coin_value, total + 1):
            """
            Calculate the minimum between the current
            minimum and using the current coin.
            """
            dp[amount] = min(dp[amount], dp[amount - coin_value] + 1)

    """
    If dp[total] is still infinity, it means the total
    cannot be met by any combination of coins.
    Otherwise, return the minimum number of coins needed.
    """
    return dp[total] if dp[total] != float('inf') else -1
