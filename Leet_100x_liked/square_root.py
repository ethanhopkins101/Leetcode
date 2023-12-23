"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
#-------------------------------------------
Example 1:
Input: x = 4
Output: 2
#-------------------------------------------
Example 2:
Input: x = 8
Output: 2
#-------------------------------------------
#Approach:
One way to solve this would be to check every number starting from 0. Since we could stop once we reach the square root of x, this would run in O(sqrt(n)) time. However, binary search runs in O(log n) time, which, as you can see from the graph below, is superior to O(sqrt n) time.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid - 1
            else:
                return mid

        return right
