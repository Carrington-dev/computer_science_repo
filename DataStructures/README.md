# BFS vs DFS for Binary Tree
Last Updated : 19 Feb, 2024

__Breadth-First Search (BFS) and Depth-First Search (DFS) for Binary Trees are ways to traverse nodes of the Binary Tree. This article aims to provide the basic difference between BFS and DFS for Binary Tree.__

__A Tree is typically traversed in two ways:__
Breadth First Traversal (Or Level Order Traversal)
Depth First Traversals
Inorder Traversal (Left-Root-Right)
Preorder Traversal (Root-Left-Right)
Postorder Traversal (Left-Right-Root)

### BFS vs DFS for Binary Tree

#### What is Breadth First Search?
Breadth First Search (BFS) is a graph traversal algorithm that starts traversing the graph from the root node and explores all the neighboring nodes at the present depth prior to moving on to the nodes at the next depth level.

#### How does BFS Tree Traversal work?
Breadth First Search (BFS) traversal explores all the neighboring nodes at the present depth prior to moving on to the nodes at the next depth level. In the context of a tree, BFS traversal works similarly.

Here’s how BFS tree traversal typically works:



#### Start at the root node and add it to a queue.
While the queue is not empty, dequeue a node and visit it.
Enqueue all of its children (if any) into the queue.
Repeat steps 2 and 3 until the queue is empty.
This approach ensures that nodes are visited level by level, moving horizontally across the tree before moving to the next level. This way, BFS explores the nodes in a breadth-first manner, making it useful for tasks like finding the shortest path in unweighted graphs or trees.

#### What is a Depth-first search?
DFS (Depth-first search) is a technique used for traversing trees or graphs. Here backtracking is used for traversal. In this traversal first, the deepest node is visited and then backtracks to its parent node if no sibling of that node exists

1. Inorder Traversal (Practice):
Follow the below steps to solve the problem:

Traverse the left subtree, i.e., call Inorder(left-subtree)
#### Visit the root
Traverse the right subtree, i.e., call Inorder(right-subtree)
2. Preorder Traversal (Practice):
Follow the below steps to solve the problem:

#### Visit the root
Traverse the left subtree, i.e., call Preorder(left-subtree)
Traverse the right subtree, i.e., call Preorder(right-subtree)
3. Postorder Traversal (Practice):
Follow the below steps to solve the problem:

Traverse the left subtree, i.e., call Postorder(left-subtree)
Traverse the right subtree, i.e., call Postorder(right-subtree)
#### Visit the root.
Difference Between BFS and DFS:
#### Parameters	BFS	DFS
Stands for	BFS stands for Breadth First Search.	DFS stands for Depth First Search.
Data Structure	BFS(Breadth First Search) uses Queue data structure for finding the shortest path.	DFS(Depth First Search) uses Stack data structure.
Definition	BFS is a traversal approach in which we first walk through all nodes on the same level before moving on to the next level.  	DFS is also a traversal approach in which the traverse begins at the root node and proceeds through the nodes as far as possible until we reach the node with no unvisited nearby nodes.
__Conceptual Difference__	BFS builds the tree level by level.	DFS builds the tree sub-tree by sub-tree.
Approach used	It works on the concept of FIFO (First In First Out). 	It works on the concept of LIFO (Last In First Out).
Suitable for	BFS is more suitable for searching vertices closer to the given source.	DFS is more suitable when there are solutions away from source.
Applications	BFS is used in various applications such as bipartite graphs, shortest paths, etc.	DFS is used in various applications such as acyclic graphs and finding strongly connected components etc.
Conclusion
BFS and DFS are both efficient algorithms for traversing binary trees. The choice of which algorithm to use depends on the specific application and the desired traversal order. BFS is preferred when the goal is to visit all nodes at the same level, while DFS is preferred when exploring a branch as far as possible is more important.

"The DSA course helped me a lot in clearing the interview rounds. It was really very helpful in setting a strong foundation for my problem-solving skills. Really a great investment, the passion Sandeep sir has towards DSA/teaching is what made the huge difference." - Gaurav | Placed at Amazon

Before you move on to the world of development, master the fundamentals of DSA on which every advanced algorithm is built upon. Choose your preferred language and start learning today: 