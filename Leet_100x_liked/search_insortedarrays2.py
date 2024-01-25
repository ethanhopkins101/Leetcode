"""
There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).
Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].
Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.
You must decrease the overall operation steps as much as possible.
#-----------------------------------------------
Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true
#-----------------------------------------------
Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false
#-----------------------------------------------
#Approach:
this algorithm performs a modified binary search on a rotated sorted array with possible duplicates. It efficiently narrows down the search range based on comparisons with the target value and the properties of the array.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[left]:
                left += 1
                continue

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False
