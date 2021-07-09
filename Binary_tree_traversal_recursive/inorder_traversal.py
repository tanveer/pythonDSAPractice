def inorder_traversal(root):
    if not root:
        return []

    output = []

    output += self.inorder_travesal(root.left)
    output.append(root.val)
    output += self.inorder_travesal(root.right)

    return output
