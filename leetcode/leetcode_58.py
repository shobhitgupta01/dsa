# Leetcode 58 - Length of last word
# Given a string s consisting of words and spaces, return the length of the last word in the string.
# A word is a maximal
# substring
# consisting of non-space characters only.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_loc = -1
        w_loc = -1
        for i in range(len(s)):
            if i < len(s) - 1 and s[i + 1] != " " and s[i] == " ":
                s_loc = i
            if s[i] != " ":
                w_loc = i

        return w_loc - s_loc
