"""
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
#--------------------------------------------------------
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
#--------------------------------------------------------
Example 2:
Input: nums = [3,2,1,0,4]
Output: false
#Approach:

"""


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable = 0

        for i in range(len(nums)):
            if i > reachable:
                return False

            reachable = max(reachable, i + nums[i])

        return True
