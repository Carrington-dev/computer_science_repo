# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        all_items = []
        left_count = 0
        right_count = 0
        self.rightSideViewId(root, all_items, left_count, right_count)
        return all_items

    def rightSideViewId(self, root: Optional[TreeNode], listItems, left_count, right_count) -> List[int]:
        if root == None:
            return
        elif left_count == right_count:
            listItems.append(root.val)
        elif left_count == 0 and right_count == 0:
            listItems.append(root.val)
        elif left_count < right_count:
            listItems.append(root.val)
        self.rightSideViewId(root.right, listItems, left_count, right_count + 1)
        self.rightSideViewId(root.right, listItems, left_count + 1, right_count)
