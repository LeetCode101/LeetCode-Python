from typing import List


class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        result = []
        node_count = 1
        level = 1

        while label >= node_count * 2:
            node_count *= 2
            level += 1

        while label != 0:
            result.append(label)
            level_max = 2 ** level - 1
            level_min = 2 ** (level - 1)
            label = (level_max + level_min - label) // 2
            level -= 1

        return result[::-1]
