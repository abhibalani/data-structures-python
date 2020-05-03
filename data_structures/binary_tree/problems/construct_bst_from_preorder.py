

MIN = -1000000000
MAX = 1000000000


class Node:

    # Constructor to created a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def construct_tree_helper(root, )
def construct_tree(preorder):





def printInorder(node):
    if node is None:
        return
    printInorder(node.left)
    print
    node.data,
    printInorder(node.right)


# Driver program to test above function
pre = [10, 5, 1, 7, 40, 50]
root = construct_tree(pre)

print("Inorder traversal of the constructed tree: ")
printInorder(root)

