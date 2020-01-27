from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        self.generate(0, 0, n, '', result)

        return result

    def generate(
            self, left_parenthesis_count: int, right_parenthesis_count: int,
            n: int, parenthesis: str, result: List[str]) -> None:
        if left_parenthesis_count == n and right_parenthesis_count == n:
            result.append(parenthesis)

            return

        if left_parenthesis_count < n:
            self.generate(left_parenthesis_count + 1, right_parenthesis_count,
                          n, parenthesis + '(', result)

        if left_parenthesis_count > right_parenthesis_count \
                and right_parenthesis_count < n:
            self.generate(left_parenthesis_count, right_parenthesis_count + 1,
                          n, parenthesis + ')', result)
