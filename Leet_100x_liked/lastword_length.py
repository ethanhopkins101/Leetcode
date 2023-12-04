"""
Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal 
substring
consisting of non-space characters only.
#---------------------------------------------
Example 1:
Input: s = "Hello World"
Output: 5
#---------------------------------------------
Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
#---------------------------------------------
#Approach:
this code takes a string as input, removes leading and trailing spaces,
splits the string into words, extracts the last word, and returns the length of that last word.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stripped = s.strip()
        strList = stripped.split(" ")
        lastWord = strList[-1]
        return len(lastWord)
