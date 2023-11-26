"""
Given an array nums of distinct integers, return all the possible permutations.
You can return the answer in any order.
#-----------------------------------
Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#-----------------------------------
Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]
#-----------------------------------
#Approach:
Initialize Result: Create an empty list, result, to store the final permutations.
Define Backtracking Function: Define a recursive helper function backtrack,
which takes the remaining numbers to be permuted (nums) and the current permutation (path) as parameters.
"""


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, path):
            if not nums:
                result.append(path)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i + 1 :], path + [nums[i]])

        result = []
        backtrack(nums, [])
        return result
