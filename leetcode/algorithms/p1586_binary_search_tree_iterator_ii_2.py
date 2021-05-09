class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.next_stack = []
        self.prev_stack = []
        self.visited = set()

        current = root

        while current:
            self.next_stack.append(current)
            current = current.left

    def hasNext(self) -> bool:
        return len(self.next_stack) > 0

    def next(self) -> int:
        node = self.next_stack.pop()

        if node not in self.visited and node.right is not None:
            current = node.right

            while current:
                self.next_stack.append(current)
                current = current.left

        self.visited.add(node)
        self.prev_stack.append(node)

        return node.val

    def hasPrev(self) -> bool:
        return len(self.prev_stack) > 1

    def prev(self) -> int:
        self.next_stack.append(self.prev_stack.pop())

        return self.prev_stack[-1].val
