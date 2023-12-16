from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # sum has to be even to be partitioned
        if sum(nums) %2 !=0:
            return False

        target = sum(nums) // 2
        n = len(nums)
        # dp table
        table = [[None for j in range(target+1)] for i in range(n+1)]

        #initializing
        for j in range(1, target+1):
            table[0][j] = False

        for i in range(n+1):
            table[i][0] = True

        # calculating dp table
        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    table[i][j] = table[i-1][j-nums[i-1]] or table[i-1][j]
                else:
                    table[i][j] = table[i-1][j]
        
        return table[n][target]
    

print(Solution().canPartition([1,5,11,5]))