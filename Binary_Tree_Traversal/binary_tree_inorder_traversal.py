def inorder_traversal(root):

    if not root:
        return []

    stack = []
    output = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        output.append(curr.val)
        curr = curr.right
    return output
