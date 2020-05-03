# class newNode:
#
#     # Construct to create a new node
#     def __init__(self, key):
#         self.data = key
#         self.left = None
#         self.right = None
#
#
def isBST(root, min_node, max_node):
    if not root:
        return False

    if min_node and root.data <= min_node.data:
        return False

    if max_node and root.data >= max_node.data:
        return False

    return isBST(root.left, min_node, root) or isBST(root.right, root, max_node)
#
#
# # Driver Code
# if __name__ == '__main__':
#     root = newNode(3)
#     root.left = newNode(2)
#     root.right = newNode(5)
#     root.right.left = newNode(1)
#     root.right.right = newNode(4)
#     # root.right.left.left = newNode(40)
#     if isBST(root, None, None):
#         print("Is BST")
#     else:
#         print("Not a BST")


# Python program to check if a binary tree is bst or not


# A binary tree node
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBSTCheck(node, min, max):

    if not node:
        return True

    if node.data < min or node.data > max:
        return False

    return isBSTCheck(node.left, min, node.data-1) and isBSTCheck(node.right, node.data + 1, max)


def isBST(node, min=-10000000, max=10000000):
    return isBSTCheck(node, min, max)


root = Node(4)
root.left = Node(2)
root.right = Node(5)
root.left.left = Node(1)
root.left.right = Node(3)
root.left.right.right = Node(10)
# root.left.right.left = Node(7)

if isBST(root):
    print("Is BST")
else:
    print("Not a BST")