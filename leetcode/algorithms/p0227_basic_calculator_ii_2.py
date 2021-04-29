class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        last_operator = '+'
        digit = 0
        last_digit = 0

        for i, c in enumerate(s):
            if c.isdigit():
                digit = digit * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if last_operator == '+':
                    result += last_digit
                    last_digit = digit
                elif last_operator == '-':
                    result += last_digit
                    last_digit = -digit
                elif last_operator == '*':
                    last_digit *= digit
                elif last_operator == '/':
                    last_digit = int(last_digit / digit)

                last_operator = c
                digit = 0

        return result + last_digit
