"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
You m
#------------------------------------------------
Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
#------------------------------------------------
Example 2:
Input: n = 1, k = 1
Output: [[1]]
#Approach:
recursive function, backtrack, that generates all combinations of k numbers. We iterate over all numbers from first to n. For each number i, we add it to the current combination and then recursively generate all the combinations of the next numbers. After that, we remove i from the current combination to backtrack and try the next number.
"""


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first=1, curr=[]):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n + 1):
                curr.append(i)
                backtrack(i + 1, curr)
                curr.pop()

        output = []
        backtrack()
        return output
