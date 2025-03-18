# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        all_items = []
        self.rightSideViewId(root, all_items)
        return all_items

    def rightSideViewId(self, root: Optional[TreeNode], listItems) -> List[int]:
        if root == None:
            return
        
        listItems.append(root.val)
        self.rightSideViewId(root.right, listItems)
        # self.rightSideViewId(root.left, listItems, False)
