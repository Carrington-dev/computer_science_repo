class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def printTree(self, root):
        if root == None:
            return
        print(root.val, sep = " ", end = " ")
        self.printTree(root.left)
        self.printTree(root.right)
    
    def insertTreeNode(self, root, val):
        if root == None:
            root = TreeNode(val=val)
            if self.root == None:
                self.root = root
            return root
        elif root.val < val:
            root.right = self.insertTreeNode(root.right, val)
        else:
            root.left = self.insertTreeNode(root.left, val)
        return root
    
    def insertAsList(self, array):
        for i in array:
            self.insertTreeNode(self.root, i)
    
    

enteredValues = list(map(int, input().strip().split()))
print(enteredValues)
binaryTree = BinaryTree()
binaryTree.printTree(binaryTree.root)
binaryTree.insertAsList(enteredValues)
binaryTree.printTree(binaryTree.root)