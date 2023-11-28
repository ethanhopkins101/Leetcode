"""
Given a collection of numbers, nums,
that might contain duplicates, return all possible unique permutations in any order.
#----------------------------------------
Example 1:
Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
#----------------------------------------
Example 2:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#----------------------------------------
#Approach:
as we have duplicates in input, we can track the count of each number. Python provides a built-in lib Counter which I will be using for this problem. As the order of output results doesn't matter,
we can use this Counter variable to track visited elements in the exploration path
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        counter = Counter(nums)

        def findAllPermutations(res):
            if len(res) == len(nums):
                permutations.append(res)
                return

            for key in counter:
                if counter[key]:
                    counter[key] -= 1  # decrement visited key
                    findAllPermutations(res + [key])
                    counter[
                        key
                    ] += 1  # restore the state of visited key to find the next path

        findAllPermutations([])
        return permutations
