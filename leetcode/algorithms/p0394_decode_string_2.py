class Solution:
    def decodeString(self, s: str) -> str:
        stack = [['', 1]]
        digit = 0

        for c in s:
            if c.isdigit():
                digit = digit * 10 + int(c)
            elif c == '[':
                stack.append(['', digit])
                digit = 0
            elif c == ']':
                text, count = stack.pop()
                stack[-1][0] += text * count
            else:
                stack[-1][0] += c

        return stack[0][0]
