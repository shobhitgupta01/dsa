class Solution:
    def longestPalindrome(self, s: str) -> str:
        palSub = ""
        palLen = 0

        for i in range(len(s)):
            # odd
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palLen:
                    palLen = r - l + 1
                    palSub = s[l : r + 1]
                l -= 1
                r += 1

            # even
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > palLen:
                    palLen = r - l + 1
                    palSub = s[l : r + 1]
                l -= 1
                r += 1

        return palSub


# running examples
s1 = "babad"
s2 = "sdfggggjkjl"

sol = Solution()
print(sol.longestPalindrome(s1))
print(sol.longestPalindrome(s2))
