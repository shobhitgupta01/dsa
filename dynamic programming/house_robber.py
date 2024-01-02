# House Robber
# Leetcode 198

class Solution:
    def rob(self, nums) -> int:
        n = len(nums)
        t = [-1 for i in range(n+1)]
        t[0] = 0
        t[1] = nums[0]

        for i in range(2, n+1):
            t[i] = max(nums[i-1] + t[i-2], t[i-1])
        
        return t[n]

print(Solution().rob([2,1,1,2]))