#Mininum Opeartion Intterview qestion task

Task
0. Minimum operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6

Explanation
Initialize a variable named 'operations' to keep track of the number of operations performed. Set it to 0 initially.
Check if 'n' is less than 2. If so, it is impossible to achieve 'n' occurrences of 'H', so return 0.
Initialize a variable named 'current' to keep track of the current number of 'H' characters in the file. Set it to 1 since we already have one 'H' character in the file.
Start a loop until 'current' is equal to 'n'.
Inside the loop, check if 'n' is divisible by 'current'. If so, it means we can achieve 'n' occurrences of 'H' by performing Copy All and Paste operations.
Increment 'operations' by 1 for the Copy All operation.
Update 'current' to the new value obtained by multiplying 'current' by 2.
If 'current' is equal to 'n', break out of the loop.
If the loop is not broken and 'current' is not equal to 'n', perform a Paste operation.
Increment 'operations' by 1 for the Paste operation.
Add 'current' to the current value to reflect the addition of 'current' H characters.
If 'current' is equal to 'n', break out of the loop.
After the loop ends, return the value of 'operations' as the minimum number of operations required.
