"""#--------------------------------------
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
#--------------------------------------
Example 1:
Input: s = "aa", p = "a"
Output: false
#--------------------------------------
Example 2:
Input: s = "aa", p = "*"
Output: true
#--------------------------------------
#Approach:
We set up some variables that keep track of positions and states (s_cur, p_cur, match, star) as we move through the string and pattern.
(Loop) While we haven't reached the end of the string, we check the following:
If the current character in the pattern matches the current character in the string or if the pattern character is a question mark, we move forward in both the string and pattern.
If we encounter a '*' in the pattern, we note down the current positions in the string and pattern and move the pattern position forward.
If none of the above conditions are met, but we have seen a '' before, we reset the pattern position after the '' to the next character, increment the match counter, and move the string position to the new match.
If none of the conditions are met mainly (p_cur reaches the end) and we have no '*' to fall back on, we know the pattern doesn't match the string, so we return False.
After going through the string, we check if there are any '*' characters left in the pattern. If there are, we move the pattern position forward.
Finally, if we've reached the end of the pattern at this point, we know the pattern matches the string, so we return True. Otherwise, we return False.
"""


class Solution:
    def isMatch(self, s, p):
        s_cur = 0
        p_cur = 0
        match = 0
        star = -1
        while s_cur < len(s):
            if p_cur < len(p):
                print("Pattern Char", p[p_cur])
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == "?"):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur < len(p) and p[p_cur] == "*":
                match = s_cur
                star = p_cur
                p_cur = p_cur + 1
            elif star != -1:
                p_cur = star + 1
                match = match + 1
                s_cur = match
            else:
                return False
        while p_cur < len(p) and p[p_cur] == "*":
            p_cur = p_cur + 1

        if p_cur == len(p):
            return True
        else:
            return False
