import collections
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int],
                                rightChild: List[int]) -> bool:
        root = 0
        children = set(leftChild + rightChild)

        for i in range(n):
            if i not in children:
                root = i

        visited = set()
        queue = collections.deque([root])

        while queue:
            node = queue.popleft()

            if node in visited:
                return False

            visited.add(node)

            if leftChild[node] != -1:
                queue.append(leftChild[node])

            if rightChild[node] != -1:
                queue.append(rightChild[node])

        return len(visited) == n
