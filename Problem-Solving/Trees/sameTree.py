# Definition for singly-linked list.
from typing import Optional

class BinaryTree:
    def __init__(self):
        self.head = None
        
    def insert(self, head,  x):
        if( head is None ):
            head  = TreeNode(x)
            if self.head is None:
                self.head = head
            return head
        if head.val < x:
            head.left = self.insert(head.left, x)
        else:
            head.right = self.insert(head.right, x)
        return head
    
    def print(self, head):
        if head == None:
            return 
        print(head.val, sep=" ", end=" ")
        self.print(head.left)
        self.print(head.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self) -> str:
        return f"{ self.val }"
    
def compareNodes(head_one: TreeNode, head_two: TreeNode):
    if head_one == None and head_two == None:
        return True
    if (head_one != None and head_two == None) or (head_one == None and head_two != None):
        return False
    if head_one.val != head_two.val:
        return False
    output1 = compareNodes(head_one.left, head_two.left)
    output2 = compareNodes(head_one.right, head_two.right)
    return output1 == output2


listt = BinaryTree()
listt2 = BinaryTree()

x = int(input())
while x != -1:
    listt.insert(listt.head, x)
    x = int(input())


x = int(input())
while x != -1:
    listt2.insert(listt2.head, x)
    x = int(input())

listt.print(listt.head)
print()
listt2.print(listt2.head)
print()
print(compareNodes(listt.head, listt2.head))

"""
25
20
36
10
22
30
40
5
12
28
38
48
-1
25
23
36
10
22
30
40
5
12
28
38
48
-1

Same
25 23 34
25 23 34

Different
25 24 34
25 23 34

Different
25 24
25 23 34

.
25 23 34



        

    def compareNodes(head_one: TreeNode, head_two: TreeNode):
        if head_one == None and head_two == None:
            return True
        if (head_one != None and head_two == None) or (head_one == None and head_two != None):
            return False
        if head_one.val != head_two.val:
            return False
        output1 = compareNodes(head_one.left, head_two.left)
        output2 = compareNodes(head_one.right, head_two.right)
        return output1 == output2

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p:
            return not q
        elif not q:
            return not p
        elif not q and not p:
            return True

        return p and q and p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
