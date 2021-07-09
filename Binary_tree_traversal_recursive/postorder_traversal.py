def postorder_traversal(root):
    if not root:
        return []
    output = []

    output += self.postorder_traversal(root.left)
    output += self.postorder_traversal(root.right)
    output.append(root.val)

    return output
