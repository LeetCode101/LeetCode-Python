import collections
import string
from typing import List


# Memory Limit Exceeded!
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> List[List[str]]:
        words = set(wordList)
        queue = collections.deque([(beginWord, 1, set(), [beginWord])])
        letters = string.ascii_lowercase
        result = []
        min_length = len(wordList)

        if endWord not in words:
            return []

        while queue:
            word, length, visited, words_so_far = queue.popleft()

            if word == endWord:
                if length < min_length:
                    min_length = length
                    result = [words_so_far]
                elif length == min_length:
                    result.append(words_so_far)

                continue

            for i in range(len(word)):
                for c in letters:
                    new_word = word[:i] + c + word[i + 1:]

                    if new_word in words and new_word not in visited:
                        queue.append((new_word, length + 1,
                                      visited | {new_word},
                                      words_so_far + [new_word]))

        return result
