class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        digit = 0
        last_sign = 1
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                digit = digit * 10 + int(c)

                if i == len(s) - 1 or not s[i + 1].isdigit():
                    result += last_sign * digit
                    digit = 0
            elif c == '+':
                last_sign = 1
            elif c == '-':
                last_sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(last_sign)

                result = 0
                last_sign = 1
            elif c == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result

        return result
