"""
You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.
Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
The testcases are generated so that the answer will be less than or equal to 2 * 109.
#------------------------------------
Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
#------------------------------------
Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1
#------------------------------------
#Approach:
Check out the Populated grid here :
[7, 3, 3, 1]
[4, 0, 2, 1]
[4, 2, 1, 1]
[2, 1, 0, 1]
[1, 1, 1, 1]
This is for input
[0,0,0,0]
[0,1,0,0]
[0,0,0,0]
[0,0,1,0]
[0,0,0,0]
"""


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dfsStack = []

        direction = [(1, 0), (0, 1)]

        if obstacleGrid[m - 1][n - 1] == 1 or obstacleGrid[0][0]:
            return 0

        memo = [[0 for _ in range(n)] for _ in range(m)]

        # inititalise the memo for the dest
        memo[m - 1][n - 1] = 1

        def recurDFS(i, j):
            if obstacleGrid[i][j] == 1:
                return 0

            if memo[i][j] != 0:
                return memo[i][j]

            for x, y in direction:
                # print(x,y)
                dx = i + x
                dy = j + y

                if 0 <= dx < m and 0 <= dy < n:
                    # print(">",dx,dy)
                    memo[i][j] += recurDFS(dx, dy)

            return memo[i][j]

        recurDFS(0, 0)
        for i in range(m):
            print(memo[i])
        return memo[0][0]
