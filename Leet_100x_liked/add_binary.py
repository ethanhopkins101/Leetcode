"""
Given two binary strings a and b, return their sum as a binary string.
#---------------------------------------------
Example 1:
Input: a = "11", b = "1"
Output: "100"
#---------------------------------------------
Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
#---------------------------------------------
#Approach:
We start at the right end of each binary number, adding the digits and any carry-over value, and storing the result in a new string.
Now we move to the next digit on the left and repeats the process until it has gone through all the digits in both binary numbers.
If there is any carry-over value after adding all the digits, append it to the end of the new string.
Finally, the new string is reversed and returned as the sum of the two binary numbers.
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s = []
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += int(a[i])
                i -= 1
            if j >= 0:
                carry += int(b[j])
                j -= 1
            s.append(str(carry % 2))
            carry //= 2

        return "".join(reversed(s))
