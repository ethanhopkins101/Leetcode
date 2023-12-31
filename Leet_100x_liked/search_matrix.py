"""
You are given an m x n integer matrix matrix with the following two properties:
Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.
You must write a solution in O(log(m * n)) time complexity.
#---------------------------------------------
Example1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
#---------------------------------------------
Example2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
#---------------------------------------------
#Approach:
Given the problem, it may be tempting to perform a linear search through the entire matrix, but this would result in a time complexity of O(m×n)O(m \times n)O(m×n), which is not acceptable given the problem's constraint of O(log⁡(m×n))O(\log(m \times n))O(log(m×n)).
Instead, we can leverage the fact that the matrix is sorted both row-wise and column-wise, and apply a binary search to find the target.
"""


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row, mid_col = divmod(mid, n)

            if matrix[mid_row][mid_col] == target:
                return True
            elif matrix[mid_row][mid_col] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
