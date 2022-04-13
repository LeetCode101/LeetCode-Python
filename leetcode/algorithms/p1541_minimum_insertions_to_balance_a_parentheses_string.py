class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        missing_left = 0
        missing_right = 0
        i = 0
        n = len(s)

        while i < n:
            c = s[i]

            if c == '(':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
                else:
                    missing_left += 1

                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    missing_right += 1

            i += 1

        return len(stack) * 2 + missing_left + missing_right
