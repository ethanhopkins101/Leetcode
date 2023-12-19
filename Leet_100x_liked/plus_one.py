"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
#---------------------------------------------------
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
#---------------------------------------------------
Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
#---------------------------------------------------
#Approach:
Instead of looping across the list and accounting for random 9s, just convert to an integer and add one. Then convert back to a list.
"""


class Solution:
    def plusOne(self, digits):
        strings = ""
        for number in digits:
            strings += str(number)

        temp = str(int(strings) + 1)

        return [int(temp[i]) for i in range(len(temp))]
