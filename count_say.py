"""
The count-and-say sequence is a sequence of digit strings defined by
the recursive formula:
countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of
substrings such that each substring contains exactly one unique digit. Then for each
substring, say the number of digits, then say the digit. Finally, concatenate every said digit.
#-----------------------------------
Example 1:
Input: n = 1
Output: "1"
#-----------------------------------
Example 2:
Input: n = 4
Output: "1211"
#-----------------------------------
#Approach:
 recursive approach to generate the sequence of strings. If n is equal to 1,
 we simply return the string "1" as it is the first string in the sequence. Otherwise,
 we recursively call the countAndSay function with n-1
 to get the previous string in the sequence. We then iterate through the previous string and apply the count-and-say algorithm to generate the current string in the sequence.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        prev = self.countAndSay(n - 1)
        result = ""
        count = 1
        digit = prev[0]
        for i in range(1, len(prev)):
            if prev[i] == digit:
                count += 1
            else:
                result += str(count) + digit
                count = 1
                digit = prev[i]
        result += str(count) + digit
        return result
