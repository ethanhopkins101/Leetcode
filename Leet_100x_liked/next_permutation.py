"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.
For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
#------------------------------------
Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]
#------------------------------------
Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]
#------------------------------------
Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
#------------------------------------
#Approach:
If the number is sorted in decreasing order, then we know that it must wrap around to nums sorted in increasing order
Then, we make a single pass starting from the end of the array. Our goal is to find that pair (a, b).
Once we identify a, we search from b forward to identify the smallest value above a, which we'll call "c".
We make the swap between "a" and "c".
Finally, we just sort from b onward.
"""


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Base case
        if nums == sorted(nums, key=lambda x: -x):
            nums.sort()
            return

        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                # Find the first value that is less than the current value
                min_idx, min_val = len(nums), float("inf")
                for j in range(len(nums) - 1, i - 1, -1):
                    if nums[j] > nums[i - 1] and nums[j] < min_val:
                        min_val = nums[j]
                        min_idx = j
                nums[i - 1], nums[min_idx] = nums[min_idx], nums[i - 1]

                # Bubble Sort
                while True:
                    swapped = False
                    for k in range(i, len(nums) - 1):
                        if nums[k] > nums[k + 1]:
                            swapped = True
                            nums[k], nums[k + 1] = nums[k + 1], nums[k]
                    if swapped == False:
                        break

                return
