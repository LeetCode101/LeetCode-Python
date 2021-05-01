class Solution:
    def calculate(self, s: str) -> int:
        last_operator = '+'
        stack = []
        digit = 0
        i, length = 0, len(s)

        while i < length:
            c = s[i]

            if c.isdigit():
                digit = digit * 10 + int(c)
            elif c == '(':
                j = i + 1
                braces = 1

                while j < length:
                    if s[j] == '(':
                        braces += 1

                    if s[j] == ')':
                        braces -= 1

                    if braces == 0:
                        break

                    j += 1

                digit = self.calculate(s[i + 1:j])
                i = j

            if c in '+-*/' or i == length - 1:
                if last_operator == '+':
                    stack.append(digit)
                elif last_operator == '-':
                    stack.append(-digit)
                elif last_operator == '*':
                    stack.append(stack.pop() * digit)
                elif last_operator == '/':
                    stack.append(int(stack.pop() / digit))

                digit = 0
                last_operator = c

            i += 1

        return sum(stack)
