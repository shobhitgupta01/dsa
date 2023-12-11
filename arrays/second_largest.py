class Solution:

    def second_largest(self, arr):
        first = arr[0]
        for i in range(1,len(arr)):
            if arr[i]>first:
                second = first
                first = arr[i]
            elif second < arr[i] < first:
                second = arr[i]
        
        return second
    

sol = Solution()
list = [99,1000,3,4,5,6]
res = sol.second_largest(list)
print(res)
