def inorder(root):
    values = []

    _inorder(root, values)

    return values


def _inorder(root, values):
    if not root:
        return

    _inorder(root.left, values)

    values.append(root.val)

    _inorder(root.right, values)


def preorder(root):
    values = []

    _preorder(root, values)

    return values


def _preorder(root, values):
    if not root:
        return

    values.append(root.val)

    _preorder(root.left, values)
    _preorder(root.right, values)
