import collections
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) \
            -> List[TreeNode]:
        roots = {root.val: root}
        delete_set = set(to_delete)
        queue = collections.deque([(root, None)])

        while queue:
            node, parent = queue.popleft()
            deleted = node.val in delete_set

            if deleted:
                if node.val in roots:
                    roots.pop(node.val)

                if parent:
                    if parent.left is node:
                        parent.left = None
                    elif parent.right is node:
                        parent.right = None

                if node.left:
                    roots[node.left.val] = node.left

                if node.right:
                    roots[node.right.val] = node.right

            if node.left:
                queue.append((node.left, node if not deleted else None))

            if node.right:
                queue.append((node.right, node if not deleted else None))

        return roots.values()
