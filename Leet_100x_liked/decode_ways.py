"""
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".
Given a string s containing only digits, return the number of ways to decode it.
The test cases are generated so that the answer fits in a 32-bit integer.
#--------------------------------------------
Example 1:
Input: s = "12"
Output: 2
#--------------------------------------------
Example 2:
Input: s = "226"
Output: 3
#--------------------------------------------
#Approach:
1. Check if the input string s is empty or starts with '0'. If so, return 0 because a valid decoding is not possible.
2. Initialize a dynamic programming array dp of size n + 1, where n is the length of the input string. Set dp[0] and dp[1] to 1, as there is one way to decode an empty string and a string of length 1.
3. Iterate through the string starting from index 2 up to n + 1.
Convert the current one-digit and two-digit substrings to integers.
If the one-digit substring is not '0', update dp[i] by adding dp[i - 1] because we can consider the current digit as a single character.
If the two-digit substring is between 10 and 26 (inclusive), update dp[i] by adding dp[i - 2] because we can consider the current two digits as a single character.
4.The final result is stored in dp[n], where n is the length of the input string.
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])
            two_digits = int(s[i - 2 : i])

            if one_digit != 0:
                dp[i] += dp[i - 1]

            if 10 <= two_digits <= 26:
                dp[i] += dp[i - 2]

        return dp[n]
