class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, score = [], 0

        for c in s:
            if c == '(':
                stack.append(score)
                score = 0
            else:
                score += stack.pop() + max(score, 1)

        return score
