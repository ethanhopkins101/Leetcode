'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
#------------------------------------------
Example 1:

Input: s = "()"
Output: true
#------------------------------------------
Example 2:
Input: s = "()[]{}"
Output: true
#------------------------------------------
Example 3:
Input: s = "(]"
Output: false
#------------------------------------------
#Approach:
iterate through the input string s character by character.
We maintain a stack to keep track of open brackets encountered.
When we encounter an open bracket ('(', '{', or '['), we push it onto the stack.
When we encounter a closing bracket (')', '}', or ']'),
we check if there is a matching open bracket at the top of the stack. If not,
it means the brackets are not balanced, and we return false.
 If there is a matching open bracket, we pop it from the stack.
At the end of the loop, if the stack is empty, it indicates that all open brackets have been closed properly, and we return true. Otherwise,
if there are unmatched open brackets left in the stack, we return false.
'''
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        
        for c in s:
            if c in '({[':
                brackets.append(c)
            else:
                if not brackets:
                    return False 
                open_bracket = brackets.pop()
                
                if (c == ')' and open_bracket != '(') or (c == '}' and open_bracket != '{') or (c == ']' and open_bracket != '['):
                    return False 
        
        return not brackets