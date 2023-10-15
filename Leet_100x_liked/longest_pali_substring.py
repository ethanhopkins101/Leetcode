#Given a string s, return the longest palindromicsubstring in s.
'''
Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
----------------------------------------
Example 2:
Input: s = "cbbd"
Output: "bb"

#Approach:
Start from the outside of the string so that we are checking increasingly lesser lengths
 of the sub strings throughout the iterations and stop when a palindromic substring is found,
 so that we find the optimal (longest substring) first before we even get to the sub-optimal strings.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        for i in range(len(s), 0, -1):
            for j in range(len(s)-i+1):
                sub = s[j:j+i]
                if sub == sub[::-1]:
                    return sub
        return ''
