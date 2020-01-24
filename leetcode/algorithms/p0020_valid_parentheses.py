class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []

        for c in s:
            if c in parentheses:
                stack.append(c)
            else:
                if not stack:
                    return False

                left = stack.pop()

                if parentheses[left] != c:
                    return False

        return not stack
