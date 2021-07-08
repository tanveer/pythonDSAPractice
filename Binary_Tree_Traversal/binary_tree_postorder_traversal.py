def postorder_traversal(root):

    if not root:
        return []
    stack = []
    stack.append(root)
    output = []

    while stack:
        last_node = stack.pop()

        if last_node.left:
            stack.append(last_node.left)
        if last_node.right:
            stack.append(last_node.right)
        output.append(last_node.val)

    return output[::-1]
