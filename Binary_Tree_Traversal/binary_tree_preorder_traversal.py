def preorder_traversal(root):
    if not root:
        return []

    stack = []
    output = []
    curr = root

    while stack or curr:
        while curr:
            stack.append(curr)
            output.append(curr.val)
            curr = curr.left

        curr = stack.pop()
        curr = curr.right

    return output
