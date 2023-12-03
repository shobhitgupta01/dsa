def findLCS(s1: str, s2: str) -> str:
    """Function to return the Longest Common Subsequence"""
    n = len(s1)
    m = len(s2)

    # creating the dp table
    t = [[0 for j in range(m+1)]for i in range(n+1)]

    # filling values in the dp table
    for i in range(1,n+1):
        for j in range(1,m+1):
            if s1[i-1] == s2[j-1]:
                t[i][j] =  1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j], t[i][j-1])
    
    # t[n][m] contains the length of longest common subsequence

    # printing the lcs
    lcs = []
    i,j = n,m
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            lcs.insert(0,s1[i-1])
            i-=1
            j-=1
        else:
            if t[i-1][j] > t[i][j-1]:
                i-=1
            else:
                j-=1
    
    return ''.join(lcs)



s1 = 'acbcf'
s2 = 'abcdaf'

print(findLCS(s1, s2))
