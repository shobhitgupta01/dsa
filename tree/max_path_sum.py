# Definition for a binary tree node.
# Leetcode 124
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root) -> int:

        res = float('-inf')

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            # case if node may not be root of the path
            temp = max(node.val, node.val + max(left, right))
            # case if node may be the root of the path
            ans = max(temp, node.val + left + right)
            # storing the max path sum
            res = max(res, ans)

            return temp

        dfs(root)

        return res
        
left = TreeNode(2)
right = TreeNode(3)

treeRoot = TreeNode(val = 1, left=left, right=right)

print(Solution().maxPathSum(treeRoot))