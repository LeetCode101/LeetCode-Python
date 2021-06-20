import collections
import string
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> int:
        words = set(wordList)
        visited = set()
        queue = collections.deque([(beginWord, 1)])
        letters = string.ascii_lowercase

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for c in letters:
                    new_word = word[:i] + c + word[i + 1:]

                    if new_word in words and new_word not in visited:
                        queue.append((new_word, length + 1))
                        visited.add(new_word)

        return 0
