## Making change

# Task
0. Change comes from within
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task

carrie@ubuntu:~/0x08-making_change$ cat 0-main.py
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

print(makeChange([1, 2, 25], 37))

print(makeChange([1256, 54, 48, 16, 102], 1453))

carrie@ubuntu:~/0x08-making_change$
carrie@ubuntu:~/0x08-making_change$ ./0-main.py
7
-1
carrie@ubuntu:~/0x08-making_change$


Solution explanation
We still check if the total is less than or equal to zero to handle special cases where no coins are needed.

We use an array called dp to store the minimum number of coins needed for each amount from 0 to the total. We initialize all values in this array to infinity except for dp[0], which is set to 0 because we don't need any coins to make 0.

We iterate through each coin's value in the coins list and for each coin, we go through all possible amounts from its value to the total.

For each amount, we calculate the minimum number of coins needed by comparing the current minimum (stored in dp[amount]) with the number of coins needed to make the remaining amount after subtracting the current coin's value (i.e., dp[amount - coin_value] + 1, where 1 represents using one more coin).

Finally, if dp[total] is still infinity, it means that we couldn't make the total with the given coins, so we return -1. Otherwise, we return the minimum number of coins needed, which is stored in dp[total].
