from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        result = []

        self._dfs(num, '', 0, 0, 0, target, result)

        return result

    def _dfs(self, num, expression_so_far, current_value,
             last_digit, position, target, result):
        if position == len(num):
            if current_value == target:
                result.append(expression_so_far)

        for i in range(position, len(num)):
            if i != position and num[position] == '0':
                break

            digit_str = num[position:i + 1]
            digit = int(digit_str)

            if position == 0:
                self._dfs(num, expression_so_far + digit_str, digit,
                          digit, i + 1, target, result)
            else:
                self._dfs(num, expression_so_far + '+' + digit_str,
                          current_value + digit, digit, i + 1, target, result)
                self._dfs(num, expression_so_far + '-' + digit_str,
                          current_value - digit, -digit, i + 1, target, result)
                self._dfs(num, expression_so_far + '*' + digit_str,
                          current_value - last_digit + last_digit * digit,
                          last_digit * digit, i + 1, target, result)
