"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.
#Approach:
Brute force using O(m*n) space: The initial approach is to start with creating another matrix to store the result. From doing that, you'll notice that we want a way to know when each row and col should be changed to zero. We don't want to prematurely change the values in the matrix to zero because as we go through it, we might change a row to 0 because of the new value.
"""


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = len(matrix)
        n = len(matrix[0])

        first_row_has_zero = False
        first_col_has_zero = False

        # iterate through matrix to mark the zero row and cols
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    if row == 0:
                        first_row_has_zero = True
                    if col == 0:
                        first_col_has_zero = True
                    matrix[row][0] = matrix[0][col] = 0

        # iterate through matrix to update the cell to be zero if it's in a zero row or col
        for row in range(1, m):
            for col in range(1, n):
                matrix[row][col] = (
                    0
                    if matrix[0][col] == 0 or matrix[row][0] == 0
                    else matrix[row][col]
                )

        # update the first row and col if they're zero
        if first_row_has_zero:
            for col in range(n):
                matrix[0][col] = 0

        if first_col_has_zero:
            for row in range(m):
                matrix[row][0] = 0
