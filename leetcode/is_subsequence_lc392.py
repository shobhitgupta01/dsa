class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1
        
        s_list = list(s)

        for char in t:
            if s_map.get(char,0) > 0 and char == s_list[0]:
                s_map[char] = s_map[char] -1
                s_list.pop(0)
        
        return len(s_list) == 0


print(Solution().isSubsequence('atr','abctr'))

print(Solution().isSubsequence('art','abctr'))