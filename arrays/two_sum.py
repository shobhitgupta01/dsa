# Leetcode 1
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [hashmap[target - nums[i]],i]
            else:
                hashmap[nums[i]] = i

print(Solution().twoSum([2,7,11,15], 9))