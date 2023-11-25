"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
#-----------------------------------
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
#-----------------------------------
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"
#-----------------------------------
#Approach:

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.strint(num1) * self.strint(num2))

    def strint(self, n):
        result = 0
        for i in range(len(n)):
            result = result * 10 + ord(n[i]) - ord("0")
        return result
