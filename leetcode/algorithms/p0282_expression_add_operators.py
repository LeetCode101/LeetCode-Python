from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                expression_so_far = num[:i]
                current_value = int(expression_so_far)
                last_value = int(expression_so_far)

                self._dfs(num[i:], expression_so_far, current_value, last_value, result, target)

        return result

    def _dfs(self, num, expression_so_far, current_value, last_value, result, target):
        if not num:
            if current_value == target:
                result.append(expression_so_far)

            return

        for i in range(1, len(num) + 1):
            digits = num[:i]

            if i == 1 or (i > 1 and num[0] != '0'):
                self._dfs(num[i:], expression_so_far + '+' + digits, current_value + int(digits), int(digits), result, target)
                self._dfs(num[i:], expression_so_far + '-' + digits, current_value - int(digits), -int(digits), result, target)
                self._dfs(num[i:], expression_so_far + '*' + digits, current_value - last_value + last_value * int(digits), last_value * int(digits), result, target)
