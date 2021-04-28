class Solution:
    def calculate(self, s: str) -> int:
        last_sign = '+'
        stack = []
        digit = 0

        for i, c in enumerate(s):
            if c.isdigit():
                digit = digit * 10 + int(c)

            if c in '+-*/' or i == len(s) - 1:
                if last_sign == '+':
                    stack.append(digit)
                elif last_sign == '-':
                    stack.append(-digit)
                elif last_sign == '*':
                    stack.append(stack.pop() * digit)
                elif last_sign == '/':
                    stack.append(int(stack.pop() / digit))

                digit = 0
                last_sign = c

        return sum(stack)
