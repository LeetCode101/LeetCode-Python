class Solution:
    def calculate(self, s: str) -> int:
        sign = '+'
        stack = []
        digit = 0

        for i, c in enumerate(s):
            if c.isdigit():
                digit = digit * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(digit)
                elif sign == '-':
                    stack.append(-digit)
                elif sign == '*':
                    stack.append(stack.pop() * digit)
                elif sign == '/':
                    stack.append(int(stack.pop() / digit))

                digit = 0
                sign = c

        return sum(stack)