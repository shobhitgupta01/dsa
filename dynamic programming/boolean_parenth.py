# Given a boolean expression S of length N with following symbols.
# Symbols
#     'T' ---> true
#     'F' ---> false
# and following operators filled between symbols
# Operators
#     &   ---> boolean AND
#     |   ---> boolean OR
#     ^   ---> boolean XOR
# Count the number of ways we can parenthesize the expression so that the value of expression evaluates to true.

# Note: The answer can be large, so return it with modulo 1003

class Solution:
    def countWays(self, N, S):
        # code here
        mp = {}
        mod = 1003
        
        def solve(S, i, j , isTrue): 
            # base conditions
            if i>j:
                return 0
            if i== j and isTrue:
                return 1 if S[i] == 'T' else 0
            elif i==j and (not isTrue):
                return 1 if S[i] == 'F' else 0
            
            #searching in map
            key = str(i) +str(j) + str(isTrue)
       
            if key in mp:
                return mp[key]
                
            # considering diff partitions
            ans = 0
            for k in range(i+1,j,2):
                lT = solve(S, i, k-1, True)
                lF = solve(S, i, k-1, False)
                rT = solve(S, k+1, j, True)
                rF = solve(S, k+1, j, False)
                
                if S[k] == '&':  # AND
                    if isTrue:
                        ans = (ans +  (lT * rT)%mod)%mod
                    else:
                        ans = (ans + (lT*rF)%mod + (lF*rT)%mod + (lF*rF)%mod) %mod
                        
                elif S[k] == '|': # OR
                    if isTrue:
                        ans = (ans + (lT*rT)%mod + (lT*rF)%mod + (lF * rT)%mod) %mod
                    else:
                        ans = (ans + (lF * rF)%mod) %mod
                elif S[k] == '^': # XOR
                    if isTrue:
                        ans = (ans + (lT*rF)%mod + (lF*rT)%mod) %mod
                    else:
                        ans = (ans + (lT*rT)%mod + (lF*rF)%mod) %mod
            
            mp[key] = ans
            return mp[key]
                
                
        return solve(S, 0, N-1, True)
    

exp = "T|F^F&T|F^F^F^T|T&T^T|F^T^F&F^T|T^F"

print(Solution().countWays(len(exp), exp)) #638