def preorder_traversal(root):
    if not root:
        return []

    output = []

    output.append(root.val)
    output += self.preorder_traversal(root.left)
    output += self.preorder_traversal(root.right)

    return output
