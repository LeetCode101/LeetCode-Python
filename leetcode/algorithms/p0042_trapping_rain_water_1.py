from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0

        for i in range(1, len(height) - 1):
            left_max = max(height[0:i], default=0)
            right_max = max(height[i+1:], default=0)
            left_right_min = min(left_max, right_max)

            if left_right_min > height[i]:
                count += left_right_min - height[i]

        return count
