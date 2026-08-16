# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def s(a, b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and s(a.left, b.right) and s(a.right, b.left)
        return s(root.left, root.right)
