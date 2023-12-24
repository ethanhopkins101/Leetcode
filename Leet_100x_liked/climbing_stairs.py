"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#------------------------------------------------
Example 1:
Input: n = 2
Output: 2
#------------------------------------------------
Example 2:
Input: n = 3
Output: 3
#------------------------------------------------
#Approach:
The recursive solution uses the concept of Fibonacci numbers to solve the problem. It calculates the number of ways to climb the stairs by recursively calling the climbStairs function for (n-1) and (n-2) steps. However, this solution has exponential time complexity (O(2^n)) due to redundant calculations.
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
