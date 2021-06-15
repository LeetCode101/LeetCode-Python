class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        removed = []
        left_parentheses = []

        for i, c in enumerate(s):
            if c == '(':
                left_parentheses.append(i)
            elif c == ')':
                if not left_parentheses:
                    removed.append(i)
                else:
                    left_parentheses.pop()

        all_removed = set(removed + left_parentheses)
        valid_string = []

        for i, c in enumerate(s):
            if i not in all_removed:
                valid_string.append(c)

        return ''.join(valid_string)
