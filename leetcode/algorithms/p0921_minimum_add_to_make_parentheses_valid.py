class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        missing_left = 0

        for c in s:
            if c == '(':
                stack.append(c)
            elif stack:
                stack.pop()
            else:
                missing_left += 1

        return len(stack) + missing_left
