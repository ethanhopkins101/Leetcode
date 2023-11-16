"""
Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
#-----------------------------------
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
#-----------------------------------
Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
#-----------------------------------
Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
#-----------------------------------
#Approach:
Iterate through the sorted array from left to right.
When you encounter the target element for the first time, set first to the current index.
Continue iterating to find the last occurrence of the target element and update last whenever you encounter it.
Return first and last
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1
        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i
        return [first, last]
