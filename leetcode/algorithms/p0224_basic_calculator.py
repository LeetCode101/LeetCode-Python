class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        sign = 1
        stack = []
        i, length = 0, len(s)

        while i < length:
            c = s[i]

            if c == '+':
                sign = 1
            elif c == '-':
                sign = -1
            elif c == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1
            elif c == ')':
                prev_sign = stack.pop()
                prev_result = stack.pop()
                result = prev_result + prev_sign * result
            elif c != ' ':
                start = i

                while i < len(s) and s[i].isdigit():
                    i += 1

                result += sign * int(s[start:i])
                i -= 1

            i += 1

        return result
