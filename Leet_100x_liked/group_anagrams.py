"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#-------------------------------------------------
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#-------------------------------------------------
Example 2:
Input: strs = [""]
Output: [[""]]
#-------------------------------------------------
#Approach:
groups anagrams by counting the occurrences of each letter in each string and using these counts as keys in a dictionary. It ensures that anagrams with the same character counts are grouped together,
and it returns these groups as a list of lists.
"""


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            ans[tuple(count)].append(s)

        return ans.values()
