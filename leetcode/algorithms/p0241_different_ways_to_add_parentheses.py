from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        result = []

        for i, c in enumerate(expression):
            if c not in '+-*':
                continue

            part1 = self.diffWaysToCompute(expression[0:i])
            part2 = self.diffWaysToCompute(expression[i + 1:])

            for n1 in part1:
                for n2 in part2:
                    if c == '+':
                        result.append(n1 + n2)
                    elif c == '-':
                        result.append(n1 - n2)
                    elif c == '*':
                        result.append(n1 * n2)

        if not result:
            result.append(int(expression))

        return result
