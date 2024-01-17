"""
Given an integer array nums of unique elements, return all possible 
subsets
 (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
#-----------------------------------------------
Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
#-----------------------------------------------
Example 2:
Input: nums = [0]
Output: [[],[0]]
#-----------------------------------------------
#Approach:
Using this bit string approach, we can simply iterate the bit strings of length nnn which is the same as numbers [0,2n−1][0, 2^n - 1][0,2 
n
 −1]. Then we include a given number from the original set in the output set if its corresponding bit is set in the bit string. Using bit operations we shift 1 << bit to create a bitmask for a given bit and using the & operator we can determine if it is set.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [
            [nums[bit] for bit in range(len(nums)) if i & (1 << bit)]
            for i in range(2 ** len(nums))
        ]
