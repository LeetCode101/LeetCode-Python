class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        left_parentheses = []
        removed_right_parentheses = []

        for i, c in enumerate(s):
            if c == '(':
                left_parentheses.append(i)
            elif c == ')':
                if not left_parentheses:
                    removed_right_parentheses.append(i)
                else:
                    left_parentheses.pop()

        removed = set(left_parentheses + removed_right_parentheses)
        valid_string = []

        for i, c in enumerate(s):
            if i not in removed:
                valid_string.append(c)

        return ''.join(valid_string)
