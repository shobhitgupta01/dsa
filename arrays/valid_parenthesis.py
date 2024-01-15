# Leetcode 20
# Given a string containing parenthesis, find if they are valid
class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 == 1:
            return False

        closing = {'}',')',']'}
        pair = {')':'(', ']':'[', '}':'{'}

        stack = []

        for char in s:
            if stack and char in closing and stack[-1] == pair[char]:
                stack.pop()
            else:
                stack.append(char)
        if len(stack) == 0:
            return True
        return False
    
print(Solution().isValid("[({})]{[]}"));
print(Solution().isValid("}{"))