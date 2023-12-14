class Solution:
    
    #Function to find length of shortest common supersequence of two strings.
    def shortestCommonSupersequence(self, X, Y, m, n):
        
        # dp array
        t = [[0 for j in range(n+1)] for i in range(m+1)]
        
        #filling the dp table
        for i in range(1,m+1):
            for j in range(1, n+1):
                if X[i-1] == Y[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        # it is sum of lengths of both strings minus the length of longest common subsequence
        return m + n - t[m][n]
    

res = Solution().shortestCommonSupersequence('abcd', 'xycd', 4, 4)

print(res)