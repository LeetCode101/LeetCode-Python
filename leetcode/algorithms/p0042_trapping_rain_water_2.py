from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        count, length = 0, len(height)
        left_max = [0] * length
        right_max = [0] * length
        left_max[0] = height[0]
        right_max[length - 1] = height[length - 1]

        for i in range(1, length):
            left_max[i] = max(left_max[i - 1], height[i])

        for i in range(length - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        for i in range(1, length - 1):
            left_right_min = min(left_max[i - 1], right_max[i + 1])

            if left_right_min > height[i]:
                count += left_right_min - height[i]

        return count
