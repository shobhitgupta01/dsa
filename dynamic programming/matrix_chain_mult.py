# Matric Chain multiplication
# return the min cost to multiply matrices with the dimensions given in the array
class Solution:
    def matrixMultiplication(self, N, arr):
        # code here
        # memo table
        t = [[-1 for j in range(N+1)] for i in range(N+1)]
        
        def solve(arr, i, j):
            if i>=j:
                return 0
                
            if t[i][j] !=-1:
                return t[i][j]
            
            min_cost = float('inf')
            for k in range(i,j):
                cost = solve(arr, i,k) + solve(arr, k+1,j) + arr[i-1]*arr[k]*arr[j]
            
                if cost < min_cost:
                    min_cost = cost
            
            t[i][j] =  min_cost
            return t[i][j]
        
        res = solve(arr, 1, N-1)
        return res
    
arr = [10, 30, 5, 60]
print(Solution().matrixMultiplication(len(arr), arr)) #4500