#Leetcode 66
#You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
#Increment the large integer by one and return the resulting array of digits.
#Example 1:
#
#Input: digits = [1,2,3]
#Output: [1,2,4]


 class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=carry
            carry = digits[i]//10
            digits[i]%=10
        
        if carry > 0:
            digits.insert(0, carry)
        return digits       
