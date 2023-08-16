## Interview qn on Rotate 2D Matrix

# Task
0. Rotate 2D Matrix
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

jessevhedden$ cat main_0.py
#!/usr/bin/python3
"""
Test 0x07 - Rotate 2D Matrix
"""
rotate_2d_matrix = __import__('0-rotate_2d_matrix').rotate_2d_matrix

if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)

jessevhedden$
jessevhedden$ ./main_0.py
[[7, 4, 1],
[8, 5, 2],
[9, 6, 3]]
jessevhedden$


# Soluttion
rotate_2d_matrix function takes a 2D matrix as input and first transposes the matrix by swapping elements across its main diagonal. Then, it reverses each row to achieve the 90-degree clockwise rotation in-place.

# Explanation
I define rotate_2d_matrix function which is taking one argument, the 2D matrix that I want to rotate.

Inside the function, I assign variable n whic represents the length of the matrix. Since the matrix is square (having the same number of rows and columns), its length is the number of rows or columns in the matrix.

The first operation to  transpose the matrix. 
Transposing means swapping elements across the main diagonal. This effectively flips the matrix over its diagonal. I am doing this  using two nested loops:

The outer loop runs from 0 to n-1, representing the rows of the matrix.
The inner loop runs from the current row i to n-1, representing the columns of the matrix.
Inside the loop, the elements at positions [i][j] and [j][i] are swapped. This is effectively the transpose operation.
After the transpose operation, the then proceeds to reverse each row of the matrix using reverse function. This is necessary to complete the 90-degree clockwise rotation.

I then use a to  loop iterate through each row in the matrix.
I apply the reverse() function is  to each row, which reverses the order of elements in that row.
After transpose and row reversal operations, the matrix is  rotated 90 degrees clockwise in place.

I then  provide an example of how to use the rotate_2d_matrix function:

The call rotate_2d_matrix function  matrix as an argument.
I then use a loop to  iterate  through each row of the matrix and print it to the console. And the  rotated matrix is Shown.
