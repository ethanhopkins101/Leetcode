'''
Given n pairs of parentheses, write a function to generate all
combinations of well-formed parentheses.
#---------------------------------------
Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
#---------------------------------------
Example 2:
Input: n = 1
Output: ["()"]
#---------------------------------------
#Approach:
we need a way to add “(” and “)” to all possible cases and
then find a way to validate so that we don’t generate the unnecessary ones.
The first condition is if there are more than 0 open / left brackets, we recurse with the right
ones. And if we have more than 0 right brackets, we recurse with the left ones. Left and right
are initialized with'n'- the number given.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def helper(ans, s, left, right):
            if left==0 and right==0:
                ans.append(s)
                
            if left>0:
                helper(ans, s+'(', left-1, right)
                
            if right>0 and left<right:
                helper(ans, s+')', left, right-1)
        
        ans = []
        helper(ans, '', n, n)
        
        return ans