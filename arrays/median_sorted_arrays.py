# Leetcode 4
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#The overall run time complexity should be O(log (m+n)).




class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        
        left, right = 0, n1
        while left <=right:
            partition1 = (left + right) // 2
            partition2 = ((n1 + n2) // 2) - partition1

            l1 = nums1[partition1-1] if partition1 != 0 else float("-infinity")
            l2 = nums2[partition2-1] if partition2 != 0 else float("-infinity")
            r1 = nums1[partition1] if (partition1) != n1 else float("infinity")
            r2 = nums2[partition2] if (partition2) != n2 else float("infinity")

            if l1<= r2 and l2 <= r1:  # valid case
                if (n1 + n2) %2 == 0:
                    return (max(l1,l2) + min(r1,r2))/2
                else:
                    return min(r1,r2)
            elif l1 > r2:
                right = partition1 - 1
            else:
                left = partition1 + 1


print(Solution().findMedianSortedArrays([1,2,3],[4,5]))