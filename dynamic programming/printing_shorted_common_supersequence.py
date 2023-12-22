class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
        # dp table
        t = [[0 for j in range(n+1)] for i in range(m+1)]
        # calculating the dp table for lcs
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1] == str2[j-1]:
                    t[i][j] = 1 + t[i-1][j-1]
                else:
                    t[i][j] = max(t[i-1][j], t[i][j-1])
        
        i,j = m,n
        scs = []
        while i > 0 and j > 0:
            if str1[i-1] == str2[j-1]:
                scs.insert(0,str1[i-1])
                i-=1
                j-=1
            else:
                if t[i-1][j] > t[i][j-1]:
                    scs.insert(0, str1[i-1])
                    i-=1
                else:
                    scs.insert(0, str2[j-1])
                    j-=1
        
        while i > 0:
            scs.insert(0, str1[i-1])
            i-=1
        
        while j > 0:
            scs.insert(0, str2[j-1])
            j-=1

        return ''.join(scs)

print(Solution().shortestCommonSupersequence('abac', 'cab'))