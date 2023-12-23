"""
Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
For the last line of text, it should be left-justified, and no extra space is inserted between words.
Note:
A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
#-------------------------------------------------------
Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
["This    is    an",
   "example  of text",
   "justification.  "]
#-------------------------------------------------------
Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
["What   must   be",
  "acknowledgment  ",
  "shall be        "]
#-------------------------------------------------------
#Approach:
We start by initializing empty lists for the result and the current line words.
A counter is also initialized to keep track of the total length of words in the current line.
Processing Each Word:
For each word, we check if adding the next word to the current line would make it exceed the maximum width.
If it does, we proceed to justify the current line. This involves distributing spaces among the words. The modulo arithmetic is handy here, ensuring that extra spaces are evenly spread among the words.
Once the line is justified, we reset the lists and counter for the next line.
A special case is the last line, where we simply left-justify the words.
Once all the words are processed and lines are justified, we return the result list.
"""


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur_words, cur_len = [], [], 0

        for word in words:
            if cur_len + len(word) + len(cur_words) > maxWidth:
                total_spaces = maxWidth - cur_len
                gaps = len(cur_words) - 1
                if gaps == 0:
                    res.append(cur_words[0] + " " * total_spaces)
                else:
                    space_per_gap = total_spaces // gaps
                    extra_spaces = total_spaces % gaps
                    line = ""
                    for i, w in enumerate(cur_words):
                        line += w
                        if i < gaps:
                            line += " " * space_per_gap
                            if i < extra_spaces:
                                line += " "
                    res.append(line)
                cur_words, cur_len = [], 0
            cur_words.append(word)
            cur_len += len(word)

        last_line = " ".join(cur_words)
        remaining_spaces = maxWidth - len(last_line)
        res.append(last_line + " " * remaining_spaces)

        return res
