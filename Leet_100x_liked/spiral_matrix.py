"""
Given an m x n matrix, return all elements of the matrix in spiral order.
#----------------------------------
Example 1:
 Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
#----------------------------------
Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#----------------------------------
#Approach:
We will use a while loop to traverse the matrix in a clockwise spiral order.
We will define four variables: left, right, top, bottom to represent the four boundaries of the current spiral.
We will use four for loops to traverse each edge of the current spiral in clockwise order and add the elements to the result list.
We will update the boundaries of the current spiral and continue the process until all elements have been traversed.
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        result = []

        while len(result) < rows * cols:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result
