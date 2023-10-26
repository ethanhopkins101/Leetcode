'''
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
#--------------------------------------------
Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#--------------------------------------------
Example 2:
Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
#--------------------------------------------
#Approach:
Approach
we'll use brute force
We keep four-pointers i, j, k and l.
For every quadruplet, we find the sum of A[i]+A[j]+A[k]+A[l]
If this sum equals the target, we've found one of the quadruplets
and add it to our data structure and continue with the rest
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = set()
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            ans.add(tuple(sorted((nums[i], nums[j], nums[k], nums[l]))))
        
        res = []
        for i in ans:
            res += list(i),
        return res