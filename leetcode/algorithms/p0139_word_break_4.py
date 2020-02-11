from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        words = set(wordDict)
        queue = deque([0])
        visited = [False for _ in range(len(s))]

        while queue:
            start = queue.popleft()

            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in words:
                        if end == len(s):
                            return True

                        queue.append(end)

            visited[start] = True

        return False
