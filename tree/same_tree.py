# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:  # both of them None
            return True
        if not p or not q or p.val != q.val:  # one of them None or values dont match
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
