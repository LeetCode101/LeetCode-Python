from collections import deque
from typing import List


class Solution:
    def pathSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nodes = {}
        sums = []
        queue = deque([(nums[0] // 10, 0)])

        for n in nums:
            nodes[n // 10] = n % 10

        while queue:
            node, sum_so_far = queue.popleft()
            depth = node // 10
            position = node % 10
            left = (depth + 1) * 10 + position * 2 - 1
            right = left + 1
            sum_so_far += nodes.get(node, 0)

            if left not in nodes and right not in nodes:
                sums.append(sum_so_far)

            if left in nodes:
                queue.append((left, sum_so_far))

            if right in nodes:
                queue.append((right, sum_so_far))

        return sum(sums)
