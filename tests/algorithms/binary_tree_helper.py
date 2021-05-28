def inorder(root):
    values = []

    _inorder(root, values)

    return values


def _inorder(root, values):
    if not root:
        return values

    _inorder(root.left, values)

    values.append(root.val)

    _inorder(root.right, values)
