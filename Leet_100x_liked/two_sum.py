'''Given an array of integers nums and an integer target
, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution,
and you may not use the same element twice.
You can return the answer in any order.'''
'''
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]
 '''
'''
Approach
Our Approach will involve using a container (Something to store a value ,that's easy to retreive later on), Dictionary is our best option (since we also need the indexes)

we know this problem wants us to find solution for this equation:
n1+n2=target 🎯
instead of looping twice to check for two numbers n1+n2
we will loop once and check for one number n1=target-n2🎯'''

def two_sums(nums,target):
    dict_a = {}
    for i,n in enumerate(nums):
            difference = target-n
            if difference in dict_a:
                return [dict_a[difference], i]
            else:
                dict_a[n] = i
    

nums = [2,7,11,13]
target = 9
result=two_sums(nums,target)
print(result)