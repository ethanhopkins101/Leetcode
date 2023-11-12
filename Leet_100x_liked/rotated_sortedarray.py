"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
#--------------------------------
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
#--------------------------------
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
#--------------------------------
Example 3:
Input: nums = [1], target = 0
Output: -1
#--------------------------------
#Approach:
If we can determinek, the so-called unknown pivot index, the solution becomes easier.
The key is that nums[k] is the first element in nums that is strictly less than nums[0],
so we can find it in O(logN) time with a boolean binary search.
We now have the two subrrays, nums[:k] and nums[k:], and we easily deduce in which
subarray target must lie (if it indeed does lie innums) by comparing target to nums[0].
We perform a numerical binary search on the appropriate subarray, return the index if we findtarget, otherwise we return-1.
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        k = bisect_left(nums, True, key=lambda x: x < nums[0])

        if target >= nums[0]:
            left = bisect_left(nums, target, hi=k - 1)
            return left if nums[left] == target else -1

        rght = bisect_left(nums, target, lo=k)
        return rght if rght < len(nums) and nums[rght] == target else -1
