# You are given N identical eggs and you have access to a K-floored building from 1 to K.

# There exists a floor f where 0 <= f <= K such that any egg dropped from a floor higher than f will break, and any egg dropped from or below floor f will not break.
# There are few rules given below. 

# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the eggs breaks at a certain floor, it will break at any floor above.
# Return the minimum number of moves that you need to determine with certainty what the value of f is.

class Solution:
    
    #Function to find minimum number of attempts needed in 
    #order to find the critical floor.
    def eggDrop(self,n, k):
        # code here
        
        mp = [[-1 for j in range(k+1)] for i in range(n+1)]
        
        def solve(e, f):
            if f==0 or f==1:
                return f
            if e == 1:
                return f
            
            if mp[e][f] != -1:
                return mp[e][f]
            
            min_res = float('inf')
            for k in range(1,f+1):
                temp = 1 + max(solve(e-1, k-1), solve(e, f-k))
                min_res = min(min_res, temp)
            
            mp[e][f] = min_res
            return mp[e][f]
        
        return solve(e=n, f=k)
    
