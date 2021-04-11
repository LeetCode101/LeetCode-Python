from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digits = []

        for token in tokens:
            if token not in ['+', '-', '*', '/']:
                digits.append(int(token))
            else:
                digit2 = digits.pop()
                digit1 = digits.pop()

                if token == '+':
                    digits.append(digit1 + digit2)
                elif token == '-':
                    digits.append(digit1 - digit2)
                elif token == '*':
                    digits.append(digit1 * digit2)
                elif token == '/':
                    digits.append(int(digit1 / digit2))

        return digits[0]
