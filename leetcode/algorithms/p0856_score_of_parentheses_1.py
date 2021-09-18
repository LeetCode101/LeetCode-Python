class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack, score = [], 0

        for c in s:
            if c == '(':
                stack.append(score)
                score = 0

                continue

            if score == 0:
                score = 1
            else:
                score *= 2

            score += stack.pop()

        return score
