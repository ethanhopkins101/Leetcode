"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.
#---------------------------------------
Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
#---------------------------------------
Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
#---------------------------------------
#Approach:
The code implements a dynamic programming approach to find the minimum path sum in a grid.
The algorithm uses a 2D array to store the minimum path sum to reach each position (i, j) in the grid, where i represents the row and j represents the column.
The minimum path sum to reach each position (i, j) is computed by taking the minimum of the path sum to reach the position above (i-1, j) and the position to the left (i, j-1), and adding the cost of the current position (i, j).
The minimum path sum to reach the bottom-right corner of the grid is stored in the last element of the array (grid[m-1][n-1]), where m is the number of rows and n is the number of columns in the grid.
"""


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]

        for i in range(1, n):
            grid[0][i] += grid[0][i - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

        # An Upvote will be encouraging
