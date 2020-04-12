"""Implementation of binary tree"""


class Node:
    """Node class for tree nodes"""
    def __init__(self, data):
        """Initializing node for the tree"""
        self.data = data
        self.left = None
        self.right = None


class Queue1:
    """Queue for breadth first search"""
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if len(self.items):
            return self.items.pop()

    def peek(self):
        if len(self.items):
            return self.items[-1]

    def __len__(self):
        return len(self.items)


class BinaryTree:
    """Class for Binary Tree"""
    def __init__(self, node):
        """Initialize the tree root with a node"""
        self.root = node

    def dfs_pre_order(self, node, traversal):
        """
        Method to traverse the tree in DFS preorder
        Parent(root) > Child left > Child right
        :param node: Node to traverse
        :param traversal: the string which will capture the value of the nodes traversed
        :return:
        """
        if node:
            traversal += str(node.data)
            traversal = self.dfs_pre_order(node.left, traversal)
            traversal = self.dfs_pre_order(node.right, traversal)

        return traversal

    def dfs_in_order(self, node, traversal):
        """
        Method to traverse the tree in DFS inorder
        Child left > Parent(root) > Child right
        :param node: Node to traverse
        :param traversal: the string which will capture the value of the nodes traversed
        :return:
        """
        if node:
            traversal = self.dfs_in_order(node.left, traversal)
            traversal += str(node.data)
            traversal = self.dfs_in_order(node.right, traversal)

        return traversal

    def dfs_post_order(self, node, traversal):
        """
        Method to traverse the tree in DFS postorder
        Child left > Child right > Parent(root)
        :param node: Node to traverse
        :param traversal: the string which will capture the value of the nodes traversed
        :return:
        """
        if node:
            traversal = self.dfs_post_order(node.left, traversal)
            traversal = self.dfs_post_order(node.right, traversal)
            traversal += str(node.data)

        return traversal

    def bfs(self, node, traversal):
        """
        Method for breadth first search traversal
        :param node:
        :param traversal:
        :return:
        """
        if not node:
            return

        queue1 = Queue1()
        queue1.enqueue(node)

        while len(queue1) > 0:
            traversal += str(queue1.peek().data)
            node = queue1.dequeue()
            if node.left:
                queue1.enqueue(node.left)
            if node.right:
                queue1.enqueue(node.right)

        return traversal


btree = BinaryTree(Node(1))
btree.root.left = Node(2)
btree.root.right = Node(3)
btree.root.left.left = Node(4)
btree.root.left.right = Node(5)
btree.root.right.left = Node(6)
btree.root.right.right = Node(7)

#        1
#      /   \
#     2     3
#    / \   / \
#   4   5 6   7

dfs_pre_order = btree.dfs_pre_order(btree.root, '')
print('Pre order: ', dfs_pre_order)

dfs_in_order = btree.dfs_in_order(btree.root, '')
print('Post order: ', dfs_in_order)

dfs_post_order = btree.dfs_post_order(btree.root, '')
print('In order: ', dfs_post_order)

bfs = btree.bfs(btree.root, '')
print('BFS traversal: ', bfs)
