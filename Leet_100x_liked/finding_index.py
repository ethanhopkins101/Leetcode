"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#--------------------------------
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
#--------------------------------
Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
#--------------------------------
#Approach:
We can directly use the find() function on the haystack string and pass the needle string as the argument. The find() function returns the index of the first occurrence of the needle string in the haystack string,
or -1 if it is not found.
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
