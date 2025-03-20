# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        root1Nodes = []
        root2Nodes = []
        self.addToList(root1, root1Nodes)
        self.addToList(root2, root2Nodes)
        if len(root1Nodes) != len(root2Nodes):
            return False
        for i in range(len(root1Nodes)):
            if root1Nodes[i].val != root2Nodes[i].val:
                return False
        return True

    def addToList(self, root, listOfNodes):
        if root == None:
            return listOfNodes
        elif root.left == None and root.right == None:
            listOfNodes.append(root)
        self.addToList(root.left, listOfNodes) 
        self.addToList(root.right, listOfNodes) 
        return listOfNodes
