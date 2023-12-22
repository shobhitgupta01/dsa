# Min insertions to make a string palliandromic
# Leetcode 1312

class Solution:
    def minInsertions(self, s: str) -> int:
        s1 = s
        s2 = s1[::-1] # reverse string
        m,n = len(s1), len(s2)
        # dp table initialization
        t = [[0 for j in range(n+1)] for i in range(m+1)]

        # dp table calculating
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s1[i-1] == s2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        

        return m - t[m][n]
    
print(Solution().minInsertions("acdbeca"))