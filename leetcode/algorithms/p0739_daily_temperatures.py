from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        result = [0] * len(T)
        stack = []

        for i, current in enumerate(T):
            while stack and stack[-1][0] < current:
                temperature, index = stack.pop()
                result[index] = i - index

            stack.append((current, i))

        return result
