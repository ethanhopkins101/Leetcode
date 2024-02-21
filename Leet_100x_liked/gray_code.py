"""
An n-bit gray code sequence is a sequence of 2n integers where:
Every integer is in the inclusive range [0, 2n - 1],
The first integer is 0,
An integer appears no more than once in the sequence,
The binary representation of every pair of adjacent integers differs by exactly one bit, and
The binary representation of the first and last integers differs by exactly one bit.
Given an integer n, return any valid n-bit gray code sequence.
#------------------------------------------------
Example 1:
Input: n = 2
Output: [0,1,3,2]
#------------------------------------------------
Example 2:
Input: n = 1
Output: [0,1]
#------------------------------------------------
#Approach:
Create an initial list with 0
For each bit in n, starting from the 0th bit:
Traverse the current list in reverse and add the current bit to each number by doing bitwise OR with (1 << i)
This step is repeated until we have processed all the bits in n
Return the final list as the result
"""


class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            for j in range(len(res) - 1, -1, -1):
                res.append(res[j] | (1 << i))
        return res
