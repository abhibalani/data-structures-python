


def print_preorder(inorder, postorder, n):
    root = postorder[len(postorder)-1]
    if root in inorder:
        root_index = postorder.index(root)

    print(root)

    if not root_index == 0:
        print_preorder(inorder[:root_index], postorder[:root_index], len(inorder[:root_index]))

    if not root_index == n-1:
        print_preorder(inorder[root_index:], postorder[])


#          1
#       /    \
#      2       3
#    /   \      \
#   4     5      6
# # Driver Code
inorder =   [4, 2, 5, 1, 3, 6]
postorder = [4, 5, 2, 6, 3, 1]
n = len(inorder)
print('Postorder traversal')
print_preorder(inorder, postorder, n)