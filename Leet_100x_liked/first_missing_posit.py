"""
Given an unsorted integer array nums, return the smallest missing positive integer.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
#--------------------------------------
Example 1:
Input: nums = [1,2,0]
Output: 3
#--------------------------------------
Example 2:
Input: nums = [3,4,-1,1]
Output: 2
#--------------------------------------
#Approach:
Iterate through the array nums.
For each element x in the array, if x is positive and less than or equal to n, and x is not in its correct position, swap it with the element at index x - 1.
After the above step, all positive integers in the range [1, n] should be in their correct positions.
Iterate through the array nums again.
Return the first index i where nums[i] != i + 1. The result is i + 1
"""


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1
