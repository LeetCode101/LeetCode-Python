import sys
from typing import List


# Time Limit Exceeded!
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) \
            -> int:
        min_length = self._dfs(beginWord, endWord, wordList, 1, set())

        return min_length if min_length < sys.maxsize else 0

    def _dfs(self, begin_word, end_word, word_list, length, visited):
        if begin_word == end_word:
            return length

        min_length = sys.maxsize

        for word in word_list:
            if word in visited:
                continue

            if self._is_one_letter_diff(begin_word, word):
                visited.add(word)
                min_length = min(min_length, self._dfs(
                    word, end_word, word_list, length + 1, visited))
                visited.remove(word)

        return min_length

    def _is_one_letter_diff(self, a, b):
        count = 0

        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1

            if count > 1:
                return False

        return count == 1
