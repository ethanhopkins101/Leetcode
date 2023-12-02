"""
Given an integer array nums, find the 
subarray
 with the largest sum, and return its sum.
#---------------------------------------
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
#---------------------------------------
Example 2:
Input: nums = [1]
Output: 1
#---------------------------------------
#Approach:
We iterate through the nums array using a for loop, starting from the first element and going up to the last element.
For each element in the array, we add it to the current sum currentSum. This calculates the sum of the subarray ending at the current element.
Next, we check if the current sum currentSum is greater than the current maximum sum maxSum.
If the current sum currentSum becomes negative, it indicates that including the current element in the subarray would reduce the overall sum. In such cases, we reset currentSum to 0. This effectively discards the current subarray and allows us to start a fresh subarray from the next element.
We repeat steps 3 to 5 for each element in the array.
"""


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float("-inf")
        currentSum = 0

        for num in nums:
            currentSum += num

            if currentSum > maxSum:
                maxSum = currentSum

            if currentSum < 0:
                currentSum = 0

        return maxSum
