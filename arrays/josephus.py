class Solution:
    def josephus(self,n,k):
        #Your code here
        arr = list(range(1,n+1))
        res = []
        def solve(arr, i):
            if len(arr)==1:
                res.append(arr[0])
                return
            ind = (i+k-1)%len(arr)
            arr.pop(ind)
            solve(arr,ind)
            return
        
        solve(arr,0)
        return res[0]

sol = Solution()
res = sol.josephus(5,2)
print(f"Safe position : {res}")