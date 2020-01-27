from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        self.generate(n, n, '', result)

        return result

    def generate(
            self, left_parenthesis_count: int, right_parenthesis_count: int,
            parenthesis: str, result: List[str]) -> None:
        if left_parenthesis_count == 0 and right_parenthesis_count == 0:
            result.append(parenthesis)

            return

        if left_parenthesis_count > 0:
            self.generate(left_parenthesis_count - 1, right_parenthesis_count,
                          parenthesis + '(', result)

        if left_parenthesis_count < right_parenthesis_count:
            self.generate(left_parenthesis_count, right_parenthesis_count - 1,
                          parenthesis + ')', result)
