from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self) -> None:
        self.head: Node = None
    
    def insert(self, root, value):
        if root == None:
            root = Node(value)
            if self.head == None:
                self.head == root
            return root
        elif root.val < value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)
        return root


    def print(self, root):
        if root == None:
            return
        print(root.data, sep=" ", end=" ")
        self.print(root.left)
        self.print(root.right)

    def levelOrderPrinter(self, root):
        if root == None:
            return
        
        queue = deque()
        queue.append(root)
        
        output = [[root.data]]

        while len(queue) > 0:
            top = queue.pop()
            # print(top.data, sep=" ", end=" ")
            this_level = []

            if top.left != None:
                queue.append(top.left)
                this_level.append(top.left)


            if top.right != None:
                queue.append(top.right)
                this_level.append(top.right)
