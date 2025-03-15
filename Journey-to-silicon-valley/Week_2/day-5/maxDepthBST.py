# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        length = 0
        return self.maxDepthNow(root, length)

    def maxDepthNow(self, root: Optional[TreeNode], length) -> int:
        if root == None:
            return length
        left = self.maxDepthNow(root.left, length + 1)
        right = self.maxDepthNow(root.right, length + 1)

        return max(left, right)
