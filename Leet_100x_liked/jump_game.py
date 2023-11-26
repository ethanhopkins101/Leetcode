"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
#------------------------------------------
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
#------------------------------------------
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
#------------------------------------------
#Approach:
We are using a search algorithm that works by moving forward in steps and counting each step as a jump.
The algorithm keeps track of the farthest reachable position at each step and updates the number of jumps needed to reach that farthest position.
The algorithm returns the minimum number of jumps needed to reach the end of the array.
"""


class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        end = 0
        farthest = 0

        # Implicit BFS
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                ans += 1
                break
            if i == end:  # Visited all the items on the current level
                ans += 1  # Increment the level
                end = farthest  # Make the queue size for the next level

        return ans
