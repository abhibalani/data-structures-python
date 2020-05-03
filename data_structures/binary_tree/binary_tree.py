"""Implementation of binary tree"""
from data_structures.stack import Stack


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

    def pre_order(self, node, traversal):
        """
        Method to traverse the tree in DFS preorder
        Parent(root) > Child left > Child right
        :param node: Node to traverse
        :param traversal: the string which will capture the value of the nodes traversed
        :return:
        """
        if node:
            traversal += str(node.data)
            traversal = self.pre_order(node.left, traversal)
            traversal = self.pre_order(node.right, traversal)

        return traversal

    def in_order(self, node, traversal):
        """
        Method to traverse the tree in DFS inorder
        Child left > Parent(root) > Child right
        :param node: Node to traverse
        :param traversal: the string which will capture the value of the nodes traversed
        :return:
        """
        if node:
            traversal = self.in_order(node.left, traversal)
            traversal += str(node.data)
            traversal = self.in_order(node.right, traversal)

        return traversal

    def post_order(self, node, traversal):
        """
        Method to traverse the tree in DFS postorder
        Child left > Child right > Parent(root)
        :param node: Node to traverse
        :param traversal: the string which will capture the value of the nodes traversed
        :return:
        """
        if node:
            traversal = self.post_order(node.left, traversal)
            traversal = self.post_order(node.right, traversal)
            traversal += str(node.data)

        return traversal

    def level_order_traversal(self, node, traversal):
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

    def insert_level_order(self, new_node):
        node = self.root

        queue = [node]
        while len(queue) > 0:
            node = queue.pop()

            if node.left:
                queue.append(node.left)
            else:
                node.left = new_node
                break

            if node.right:
                queue.append(node.right)
            else:
                node.right = new_node
                break
        return

    def delete_deepest_node(self, node_to_delete):

        node = self.root

        queue1 = Queue1()
        queue1.enqueue(node)

        while len(queue1) > 0:
            node = queue1.dequeue()
            if node_to_delete == node:
                node = None
                return
            if node.left:
                if node.left == node_to_delete:
                    node.left = None
                    return
                else:
                    queue1.enqueue(node.left)
            if node.right:
                if node.right == node_to_delete:
                    node.right = None
                    return
                else:
                    queue1.enqueue(node.right)

    def delete(self, data):
        # curr = self.root

        queue = [self.root]
        node_to_be_deleted = None
        while len(queue) > 0:
            temp = queue.pop()
            if temp.data == data:
                node_to_be_deleted = temp
            if temp.left:
                queue.insert(0, temp.left)
            if temp.right:
                queue.insert(0, temp.right)
        if node_to_be_deleted:
            last_node_data = temp.data
            self.delete_deepest_node(temp)
            node_to_be_deleted.data = last_node_data

        return True

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

    def size(self, node):

        if not node:
            return 0

        return 1 + self.size(node.left) + self.size(node.right)


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

pre_order = btree.pre_order(btree.root, '')
print('Pre order: ', pre_order)

in_order = btree.in_order(btree.root, '')
print('In order: ', in_order)

post_order = btree.post_order(btree.root, '')
print('Post order: ', post_order)

level_order_traversal = btree.level_order_traversal(btree.root, '')
print('level_order_traversal traversal: ', level_order_traversal)

# st = btree.reverse_order_traversal(btree.root, '')
# print('Reverse traversal: ', btree.get_reverse_order(st))

btree.insert_level_order(Node(8))

level_order_traversal = btree.level_order_traversal(btree.root, '')
print('level_order_traversal traversal: ', level_order_traversal)

btree.insert_level_order(Node(9))


level_order_traversal = btree.level_order_traversal(btree.root, '')
print('level_order_traversal traversal: ', level_order_traversal)

btree.delete(2)

print('In order', str(btree.in_order(btree.root, '')))
