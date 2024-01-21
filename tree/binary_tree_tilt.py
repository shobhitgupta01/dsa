# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left, right = dfs(root.left), dfs(root.right)

            res += abs(left - right)

            return left + right + root.val

        dfs(root)
        return res
