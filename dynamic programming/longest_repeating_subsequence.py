class Solution:
    def longestRepeatingSubsequence(self, string : str)->int:
        m = n = len(string)
        t = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if (string[i-1] == string[j-1]) and i!=j:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])

        return t[m][n]
    
print(Solution().longestRepeatingSubsequence('AABCCDEFF'))


