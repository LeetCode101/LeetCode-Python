import collections
import math
from typing import List


# Time Limit Exceeded!
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        queue = collections.deque([(1, [1])])
        level = 0

        while queue:
            level += 1
            size = len(queue)
            start = int(math.pow(2, level))
            new_queue = collections.deque([])

            for i in range(size):
                node, nodes = queue.pop()

                if node == label:
                    return nodes

                a, b = start + 2 * i, start + 1 + 2 * i
                new_queue.append((a, nodes + [a]))
                new_queue.append((b, nodes + [b]))

            queue = new_queue
