# Problem statement:
# Given two strings word1 and word2, 
# return the minimum number of steps required to make word1 and word2 the same.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        # initializing the array
        t = [[0 for j in range(n+1)] for i in range(m+1)]
        # calculating the dp table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        return m + n - (2*t[m][n])
    

print(Solution().minDistance('star', 'target'))