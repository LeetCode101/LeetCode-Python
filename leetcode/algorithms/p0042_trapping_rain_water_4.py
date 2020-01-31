from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        count, i = 0, 0
        stack = []

        while i < len(height):
            while stack and height[stack[-1]] < height[i]:
                current = stack.pop()

                if not stack:
                    break

                distance = i - stack[-1] - 1
                bounded_height = \
                    min(height[i], height[stack[-1]]) - height[current]
                count += distance * bounded_height

            stack.append(i)
            i += 1

        return count
