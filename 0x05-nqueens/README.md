## Nqueens Interview question focusing on backtracking


#Task
0. Nqueens
The N queens puzzle is the challenge of placing N non-attacking queens on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
Read: Queen, Backtracking

solution
generate_solutions(row, column) function:
This function generates all the valid solutions to the N-Queens problem by placing queens on the chessboard one row at a time. It takes two parameters:

row: The current row being considered for queen placement.
column: The size of the chessboard (N).
The function starts with an initial empty solution list containing an empty list. It then iterates through each row, calling the place_queen() function to place the queen in that row. The place_queen() function returns a list of valid positions for placing the queen in the current row. The function keeps updating the solution list with each iteration, and at the end, it contains all the valid solutions.

place_queen(queen, column, prev_solution) function:
This function is responsible for placing a queen in the current row and filtering the valid positions for the next row. It takes three parameters:

queen: The row index to place the queen.
column: The size of the chessboard (N).
prev_solution: A list of previously placed queens' positions.
The function starts with an empty list called safe_position. It iterates through each array in the prev_solution list, where each array represents the positions of queens placed in the previous rows. For each array, it checks all the columns in the current row and calls the is_safe() function to verify if placing a queen at that position is safe. If it's safe, it adds the position to the safe_position list.

is_safe(q, x, array) function:
This function checks whether placing a queen at position (q, x) is safe. It takes three parameters:

q: The row index to place the queen.
x: The column index to place the queen.
array: A list representing the positions of previously placed queens.
It checks if there is a queen in the same column (x) or in the same diagonal as the current position (q, x). If there is, it returns False, indicating that it's not safe to place a queen there. Otherwise, it returns True.

init() function:
This function initializes the value of N (the size of the chessboard) based on the command-line argument. It checks if the correct number of arguments is provided and if the argument is a valid number greater than or equal to 4. If the conditions are met, it returns the value of N.

n_queens() function:
This is the main function that drives the whole process. It calls the init() function to get the value of N and then generates all the valid solutions by calling the generate_solutions() function. Finally, it prints the solutions in a clean format by converting each solution into a list of [row, column] pairs.
