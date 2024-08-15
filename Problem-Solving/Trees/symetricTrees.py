from typing import Optional


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        leftNodes = self.postorderTraversal(root.left)
        rightNodes = self.postorderTraversal(root.right)
        
        if len(leftNodes) != len(rightNodes):
            return False
        
        for i in range(len(leftNodes)):
            if leftNodes[i] != rightNodes[i]:
                return False
        
        return True
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        nums = []
        self.postorderTraversalList(root, nums)
        return nums

    def postorderTraversalList(self, root: Optional[TreeNode], nums = []) -> List[int]:
        if root == None:
            return nums
        self.postorderTraversalList(root.left, nums)
        nums.append(root.val)
        self.postorderTraversalList(root.right, nums)