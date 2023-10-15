'''
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go
 outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
------------------------------------
Example 2:
Input: x = -123
Output: -321
-------------------------------------
Example 3:
Input: x = 120
Output: 21

#Approach:
Rather than count the number of digits in advance,
we can multiply result by 10 before add the current digit from time to time.
'''
class Solution:
    def reverse(self, x):
        if x < 0:
            return -1 * self.reverseUtil(-x)
        return self.reverseUtil(x)
        
    def reverseUtil(self, x):
        result = 0
        while x != 0:
            digit = x % 10
            result = result * 10 + digit
            x = int(x / 10)
			
        return 0 if result > pow(2, 31) - 1 or result < -pow(2, 31) else result