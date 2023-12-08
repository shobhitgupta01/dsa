class Solution:

    def permutation(self,s:str):
        res = []

        def solve(input, output):
            if len(input)==0:
                res.append(output)
                return
            #with space
            solve(input[1:],output + f" {input[0]}")
            #without space
            solve(input[1:],output + f"{input[0]}")

            return
        

        solve(s[1:], f"{s[0]}")

        return res
    

sol = Solution()
res = sol.permutation("ABC")
print(res)