##0x0A. Prime Game

##Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the PEP 8 style (version 1.7.x)
All your files must be executable


##Tasks
#0. Prime Game
Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play x rounds of the game, where n may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
You can assume n and x will not be larger than 10000
You cannot import any packages in this task
Example:

x = 3, nums = [4, 5, 1]
First round: 4

Maria picks 2 and removes 2, 4, leaving 1, 3
Ben picks 3 and removes 3, leaving 1
Ben wins because there are no prime numbers left for Maria to choose
Second round: 5

Maria picks 2 and removes 2, 4, leaving 1, 3, 5
Ben picks 3 and removes 3, leaving 1, 5
Maria picks 5 and removes 5, leaving 1
Maria wins because there are no prime numbers left for Ben to choose
Third round: 1

Ben wins because there are no prime numbers for Maria to choose
Result: Ben has the most wins

## Solution
def isWinner(x, nums)::

This line defines a function named isWinner that takes two parameters, x and nums.
x represents the number of rounds.
nums is a list of integers representing the upper limits for each round.
"""...""":

This is a triple-quoted string, known as a docstring. It provides documentation for the function. It describes what the function does, what arguments it takes (Args), and what it returns (Returns).
def is_prime(num)::

This line defines a nested function named is_prime within the isWinner function.
It takes a single parameter num, which is the number to be checked for primality.
if num < 2::

This is an if statement. It checks if num is less than 2.
return False:

If the condition in the previous line is True, it means the number is not prime, and False is returned.
for i in range(2, int(num**0.5) + 1)::

This is a for loop that iterates from 2 to the square root of num (rounded up to the nearest integer).
if num % i == 0::

This is an if statement inside the loop. It checks if num is divisible evenly by i.
return False:

If the condition in the previous line is True, it means the number is not prime, and False is returned.
return True:

If none of the conditions in the loop are met, it means the number is prime, and True is returned.
def get_primes(n)::

This line defines another nested function named get_primes within the isWinner function.
It takes a single parameter n, which is the upper limit for finding prime numbers.
primes = []:

This creates an empty list called primes to store prime numbers.
for i in range(2, n + 1)::

This is a for loop that iterates from 2 to n (inclusive).
if is_prime(i)::

This line checks if i is a prime number by calling the is_prime function.
primes.append(i):

If i is prime, it is appended to the primes list.
return primes:

Finally, the list of prime numbers is returned.
def play_round(n)::

This line defines yet another nested function named play_round within the isWinner function.
It takes a single parameter n, which is the upper limit for finding prime numbers.
primes = get_primes(n):

This calls the get_primes function to get a list of prime numbers up to n and assigns it to the variable primes.
if len(primes) % 2 == 0::

This line checks if the length of the list primes (i.e., the number of prime numbers) is even.
return "Ben":

If the condition is True, it means that Ben has the advantage, and "Ben" is returned.
else::

If the condition in the previous line is False, it means that Maria has the advantage.
return "Maria":

In this case, "Maria" is returned.
round_winners = [play_round(n) for n in nums]:

This line uses a list comprehension to apply the play_round function to each element n in the nums list. It creates a list of the winners of each round.
maria_wins = round_winners.count("Maria") and ben_wins = round_winners.count("Ben"):

These lines count how many times "Maria" and "Ben" appear in the round_winners list, respectively.
The subsequent if-elif-else block compares the number of wins for Maria and Ben and determines the overall winner.

# Example Usage:

This is a comment indicating that the following lines are an example of how to use the isWinner function.
x = 3 and nums = [4, 5, 1]:

These lines assign values to the variables x and nums to demonstrate how the function works.
result = isWinner(x, nums):

This line calls the isWinner function with the provided values and assigns the result to the variable result.
print(result):

Finally, the result is printed to the console. In this example, it will output: "Ben".





