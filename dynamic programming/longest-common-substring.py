class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        max_len = 0
        t = [[0 for j in range(m+1)] for i in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                if S1[i-1] == S2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = 0
                max_len = max(max_len, t[i][j])
        
        return max_len
    

s1 = "ABCDGH"
s2 = "ACDGHR"

sol = Solution()

res = sol.longestCommonSubstr(s1, s2, len(s1), len(s2))

print(res) # should be 4 for 'CDGH'