class Solution:
    def checkValidString(self, s: str) -> bool:
        left_parenthesis = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                left_parenthesis.append(i)
            elif c == ')':
                if left_parenthesis:
                    left_parenthesis.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            elif c == '*':
                stars.append(i)

        while left_parenthesis and stars:
            if left_parenthesis[-1] < stars[-1]:
                left_parenthesis.pop()
                stars.pop()
            else:
                return False

        return not left_parenthesis
