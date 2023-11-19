"""
Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the 
frequency
 of at least one of the chosen numbers is different.
The test cases are generated such that the number of unique combinations that
sum up to target is less than 150 combinations for the given input.
#-----------------------------------------
Example 1:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
#-----------------------------------------
Example 2:
Input: candidates = [2], target = 1
Output: []
#-----------------------------------------
#Approach:
backtracking and recursive to get all possible combination
"""


class Solution:
    ans = []

    def solve(self, array, Sum, candidates, target, start):
        # print([array,Sum])
        if Sum == target:
            self.ans.append(array)
        for index in range(start, len(candidates)):
            i = candidates[index]
            if Sum + i > target:
                # print(Sum+i)
                return
            array1 = list(array)
            array1.append(i)
            Sum1 = Sum + i
            self.solve(array1, Sum1, candidates, target, index)

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        self.solve([], 0, candidates, target, 0)

        return self.ans
