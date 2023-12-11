"""
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The test cases are generated so that the answer will be less than or equal to 2 * 109.
#-------------------------------------
Example 1:
Input: m = 3, n = 7
Output: 28
#-------------------------------------
Example 2:
Input: m = 3, n = 2
Output: 3
#-------------------------------------
#Approach:
Step 1: Initialize the DP Table
Create a 2D DP (dynamic programming) table of size m x n to store the number of unique paths for each cell.
Initialize the rightmost column and bottom row of the DP table to 1 because there's only one way to reach each cell in those rows/columns (by moving all the way right or all the way down).
Step 2: Fill in the DP Table
Start from the second-to-last row and second-to-last column (i.e., i = m - 2 and j = n - 2).
For each cell (i, j) in the grid:
Calculate the number of unique paths to reach (i, j) as the sum of the unique paths from the cell below (i+1, j) and the cell to the right (i, j+1). Use this formula: dp[i][j] = dp[i+1][j] + dp[i][j+1].
Continue filling in the DP table row by row and column by column until you reach the top-left corner (dp[0][0]).
Step 3: Return the Result
Return the value stored in the top-left corner of the DP table (dp[0][0]), which represents the number of unique paths from the top-left corner to the bottom-right corner.
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Create a 2D DP table filled with zeros
        dp = [[0] * n for _ in range(m)]

        # Initialize the rightmost column and bottom row to 1
        for i in range(m):
            dp[i][n - 1] = 1
        for j in range(n):
            dp[m - 1][j] = 1

        # Fill in the DP table bottom-up
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        # Return the result stored in the top-left corner
        return dp[0][0]
