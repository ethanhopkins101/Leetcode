'''
Given an integer array nums, return all the triplets
 [nums[i], nums[j], nums[k]] such that i != j, i != k,
 and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
#----------------------------------------------------------------
Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
#----------------------------------------------------------------
Example 2:
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
#----------------------------------------------------------------
Example 3:
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
#----------------------------------------------------------------
#Approach:
First sort the array. use a for loop to iterate one index and then use two pointers approach
intilise l=i+1 and r = last then use while and check if the numbers at indices i+l+r ==0 ,
if they are then append them to the result and increment l and then check
if nums[l] == nums[l-1] then increment l till condition fails this is done to skip
the duplicates and check if sum >0 then decrement r else increment l and then return result.
Always check if i>0 and nums[i] == nums[i-1] ,
if it is then skip the iteration to skip the duplicates
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i in range(len(nums)):

            if i>0 and nums[i]==nums[i-1]:
                continue

            l = i+1
            r = len(nums)-1

            while(l<r):
                if nums[i]+nums[l]+nums[r]==0:
                    res.append([nums[i],nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1

                elif nums[i]+nums[l]+nums[r]>0:
                    r-=1

                else:
                    l+=1
        return res     