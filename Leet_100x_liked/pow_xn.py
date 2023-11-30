"""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#---------------------------------------------
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000
#---------------------------------------------
Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100
#---------------------------------------------
#Approach:
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        def function(base=x, exponent=abs(n)):
            if exponent == 0:
                return 1
            elif exponent % 2 == 0:
                return function(base * base, exponent // 2)
            else:
                return base * function(base * base, (exponent - 1) // 2)

        f = function()

        return float(f) if n >= 0 else 1 / f
