import collections


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counts = collections.Counter(s)
        chars = set()
        stack = []

        for i, c in enumerate(s):
            while stack and c < stack[-1] and counts[stack[-1]] > 0 \
                    and c not in chars:
                chars.remove(stack[-1])
                stack.pop()

            if c not in chars:
                stack.append(c)
                chars.add(c)

            counts[c] -= 1

        return ''.join(stack)
