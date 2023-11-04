"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k,
to get accepted, you need to do the following things
Change the array nums such that the first k elements of nums contain the unique
elements in the order they were present in nums initially.
The remaining elements of nums are not important as well as the size of nums.
Return k.
#-----------------------------------------
Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
#-----------------------------------------
Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
#-----------------------------------------
#Approach:
dictionary to keep track of the frequency of each element in the input list.
It then iterates over the input list, and for each element, it checks if it has
already been encountered using the dictionary. If the element is encountered for the
first time, it is added to the output list and its index is incremented. Finally,
the length of the dictionary
(which corresponds to the length of the output list) is returned.
"""


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mp = defaultdict(int)
        ans = []
        x = 0
        for i in nums:
            mp[i] += 1
            if mp[i] == 1:
                nums[x] = i
                x += 1
        return len(mp)
