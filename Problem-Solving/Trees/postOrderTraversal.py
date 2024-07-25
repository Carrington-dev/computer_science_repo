# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.postorderTraversalList(root, nums)
        return nums

    def postorderTraversalList(self, root: Optional[TreeNode], nums = []) -> List[int]:
        if root == None:
            return nums
        self.postorderTraversalList(root.left, nums)
        self.postorderTraversalList(root.right, nums)
        nums.append(root.val)