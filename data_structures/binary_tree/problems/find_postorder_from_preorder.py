

def print_post_order(inorder, preorder, n):

    if preorder[0] in inorder:
        root_index = inorder.index(preorder[0])

    if not root_index == 0:  # Left subtree exists
        print_post_order(inorder[:root_index], preorder[1:root_index+1], len(inorder[:root_index]))

    if not root_index == n-1:
        print_post_order(inorder[root_index+1:], preorder[root_index+1:], len(inorder[root_index+1:]))

    print(preorder[0])


def print_postorder(inorder, preorder, n):

    if preorder[0] in inorder:
        root_index = inorder.index(preorder[0])

    if not root_index == 0:
        print_postorder(inorder[:root_index], preorder[1:root_index+1], len(inorder[:root_index]))

    if not root_index == n-1:
        print_postorder(inorder[root_index+1:], preorder[root_index+1:], len(inorder[root_index+1:]))

    print(preorder[0])

# Driver Code
inorder = [4, 2, 5, 1, 3, 6]
preorder = [1, 2, 4, 5, 3, 6]
n = len(inorder)
print('Postorder traversal')
print_post_order(inorder, preorder, n)
print('POST ORDER')
print_postorder(inorder, preorder, n)

