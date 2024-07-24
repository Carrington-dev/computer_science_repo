# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.preorderTraversalMethod(root, nums)
        return nums

    def preorderTraversalMethod(self, root: Optional[TreeNode], nums = []) -> List[int]:
        if root == None:
            return nums
        nums.append(root.val)
        self.preorderTraversalMethod(root.left, nums)
        self.preorderTraversalMethod(root.right, nums)
        return nums
    