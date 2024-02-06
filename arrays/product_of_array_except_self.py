# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right, prod = [1] * len(nums), [1] * len(nums), [1] * len(nums)

        for i in range(1, len(nums)):
            left[i] = nums[i - 1] * left[i - 1]

        for j in range(len(nums) - 2, -1, -1):
            right[j] = nums[j + 1] * right[j + 1]

        for k in range(len(nums)):
            prod[k] = left[k] * right[k]

        return prod
