class Solution:

    def generate_parenthesis(self, n:int):

        res = []

        def solve(output, op, cl):
            if op==0 and cl==0:
                res.append(output)
                return
            
            if op==0:
                solve(output+')',op,cl-1)
            elif cl==0 or op==cl:
                solve(output+'(',op-1,cl)
            elif op < cl:
                 solve(output+'(',op-1,cl)
                 solve(output+')',op,cl-1)
            return
        
        solve('',n,n)

        return res


sol = Solution()

res = sol.generate_parenthesis(2)

print(res)