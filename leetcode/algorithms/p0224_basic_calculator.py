class Solution:
    def calculate(self, s: str) -> int:
        result = 0
        last_sign = 1
        stack = []
        i, length = 0, len(s)

        while i < length:
            c = s[i]

            if c.isdigit():
                start = i

                while i < len(s) and s[i].isdigit():
                    i += 1

                result += last_sign * int(s[start:i])
                i -= 1
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

            i += 1

        return result