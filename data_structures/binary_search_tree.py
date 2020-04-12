"""Implementation of binary search tree"""


class Node:
    """Node class for tree nodes"""
    def __init__(self, data):
        """Initializing node for the tree"""
        self.data = data
        self.left = None
        self.right = None


class BinarySearchTree:
    """Class for Binary Search Tree"""
    def __init__(self):
        """Initialize the tree root with a node"""
        self.root = None

    def insert_node(self, node):
        """
        Method to insert node in binary search tree
        :param node: node to be inserted
        :return: none
        """
        if not node:
            return

        if not self.root:
            self.root = node
        else:
            self._insert(node, self.root)
        return

    def _insert(self, node, current_node):
        """
        Helper method to traverse the tree while inserting node
        :param node: node to be inserted
        :param current_node: current node to check before inserting
        :return:
        """
        if node.data < current_node.data:
            if current_node.left:
                self._insert(node, current_node.left)
            else:
                current_node.left = node
        elif node.data > current_node.data:
            if current_node.right:
                self._insert(node, current_node.right)
            else:
                current_node.right = node
        else:
            print('Value {} already present in the tree.'.format(node.data))

    def find(self, data):
        """
        Method to find a value in one of the nodes in the tree
        :param data: value to find
        :return: none
        """
        if not self.root:
            print('Tree is empty')
            return

        is_found = self._find(data, self.root)

        if is_found:
            print('Value Found')
        else:
            print('Value not found.')
        return

    def _find(self, data, current_node):
        """
        Helper method to traverse the tree while looking for the value
        :param data: value to find
        :param current_node: node to check while traversing
        :return:
        """
        if not current_node:
            return False
        if current_node.data == data:
            return True
        elif current_node.data > data:
            return self._find(data, current_node.left)
        else:
            return self._find(data, current_node.right)

    def height(self, node):
        """
        Method to calculate height of binary tree
        :param node: node from which the height to be calculated
        :return: height of the tree (int)
        """
        if not node:
            return -1

        height_left = self.height(node.left)
        height_right = self.height(node.right)

        return 1 + max(height_left, height_right)


bst = BinarySearchTree()

#        4
#      /   \
#     2     8
#    / \   / \
#   1   3 5   10

bst.insert_node(Node(4))
bst.insert_node(Node(2))
bst.insert_node(Node(8))
bst.insert_node(Node(5))
bst.insert_node(Node(10))
bst.insert_node(Node(3))
bst.insert_node(Node(1))

bst.find(5)


height = bst.height(bst.root)

print('Tree height is: ', str(height))
